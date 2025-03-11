from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Prediction
from app.utils.ai_utils import generate_stress_suggestions
from datetime import datetime

result_bp = Blueprint('result', __name__)

@result_bp.route('/result')
@login_required
def result():
    # Fetch all predictions for the current user
    user_predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.timestamp.asc()).all()

    # Format timestamps and results for the chart
    stress_trend = [
        {
            "timestamp": p.timestamp.strftime('%Y-%m-%d'),  # Format date
            "stress_level": 1 if p.result == "Stressed" else 0 , # Convert "Stressed"/"Not Stressed" to binary
            "stress_level_eng": p.result  # Convert "Stressed"/"Not Stressed" to binary
        }
        for p in user_predictions
    ]

    # Analyze improvement trend
    stress_scores = [p["stress_level_eng"] for p in stress_trend]

    # print(f"Stress Scores: {stress_scores}")
    # print(f"Improvement: {improvement}")

    # Get the latest prediction
    latest_prediction = user_predictions[-1] if user_predictions else None
    result_message = latest_prediction.result if latest_prediction else "No prediction found."

    # Prepare AI prompt based on stress trend
    stress_summary = (
        "You are a mental wellness expert providing stress management guidance.\n\n"
        "## 🔍 User's Stress Trend Analysis\n"
        f"- Recent stress levels: {stress_trend} .\n"
        f"- Latest prediction: '{result_message}'.\n"
        "- Identify patterns and trends in the stress levels.\n"
        "- Provide a **personalized, human-like** analysis of what this trend suggests.\n"
        "- Write **as if speaking directly to the user**, using 'you' and 'your'.\n"
        "- Start suggestions with a intro line and then list the tips.\n"
        "- Avoid robotic tone; keep it warm, conversational, and supportive.\n\n"

        "### END ANALYSIS ###\n\n"

        "## 💡 Actionable Suggestions\n"
        "- Based on the trend, suggest **6-7 stress management strategies** tailored to the user's current state.\n"
        "- Ensure the advice is **practical, encouraging, and easy to implement**.\n\n"

        "**⚠️ IMPORTANT:**\n"
        "- **DO NOT** include HTML, Markdown, or styling. Keep it plain text\n"
        "- **ONLY RETURN** the analysis and suggestions as plain text.\n"
        "- **Insert the flag `### END ANALYSIS ###` before listing the suggestions points.**\n"
        "- Structure it as:\n"
        "   - First, an engaging analysis paragraph.\n"
        "   - Then, 6-7 actionable tips as `Title: Content`."
    )

    # Generate AI suggestions
    ai_suggestions = generate_stress_suggestions(stress_summary)

    # Format AI response in Python
    formatted_suggestions = format_suggestions(ai_suggestions, latest_prediction)

    return render_template(
        'result.html',
        result_message=result_message,
        additional_info=formatted_suggestions,
        stress_trend=stress_trend  # Send trend data to the frontend
    )

# Generic response to use when AI fails to generate suggestions
GENERIC_RESPONSE = """
<p class="text-gray-400 mb-5">
    Stress levels generally fluctuate, which is completely normal. The key is to focus on building resilience and maintaining balance. 
    Whether you're experiencing high stress or making progress, here are some effective ways to manage and sustain mental well-being.
</p>

<ul class="list-disc pl-6 text-gray-700">
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Mindful Breathing:</span> Take deep, slow breaths—inhale for 4 seconds, hold for 4, and exhale for 6. This can instantly reduce stress.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Identify Triggers:</span> Keep a simple stress journal to track patterns and situations that cause stress. Awareness helps with better coping strategies.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Movement & Exercise:</span> Engage in at least 10-15 minutes of light physical activity like walking or stretching to release built-up tension.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Digital Detox:</span> Take short breaks from screens and social media. Disconnecting for even 30 minutes can help reset your mind.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Healthy Sleep Routine:</span> Prioritize getting 7-8 hours of quality sleep. Avoid screens before bed and establish a calming bedtime ritual.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Hydration & Nutrition:</span> Dehydration and poor nutrition can worsen stress. Drink enough water and include whole foods in your meals.
    </li>
    <li class="mb-2 text-gray-400">
        <span class="font-medium {suggestion_class}">Social Connection:</span> Talk to a trusted friend, family member, or support group. Having a support system greatly reduces stress.
    </li>
</ul>
"""

def format_suggestions(ai_response, latest_status):
    """ Parses AI response and applies Tailwind styling dynamically. """

    # Add Tailwind CSS classes based on the latest status
    suggestion_class = "text-amber-500" if latest_status and latest_status.result == "Stressed" else "text-teal-500"

    # Check if AI response is empty or unreliable
    if not ai_response.strip() or "### END ANALYSIS ###" not in ai_response or not latest_status:
        print("⚠️ AI response is unreliable. Using fallback generic response.")
        return GENERIC_RESPONSE.format(suggestion_class=suggestion_class)  # Use the predefined generic response
    
    # Split analysis and suggestions
    if "### END ANALYSIS ###" in ai_response:
        analysis, suggestions = ai_response.split("### END ANALYSIS ###", 1)
    else:
        analysis, suggestions = ai_response, ""  # If AI fails to insert the flag

    # Move the first line of suggestions to the end of analysis
    suggestions_lines = suggestions.strip().split("\n")
    if suggestions_lines:
        suggestion_intro = suggestions_lines.pop(0)
        suggestions = "\n".join(suggestions_lines)

    # Format analysis paragraph
    formatted_html = f"<p class='text-gray-400 mb-5'>{analysis.strip()}</p>\n"

    formatted_html += f"<p class='text-gray-400 mb-5'>{suggestion_intro.strip()}</p>\n"

    # Start the suggestion list
    formatted_html += "<ul class='list-disc pl-6 text-gray-700'>\n"

    # Add suggestions to the list
    for suggestion in suggestions.split("\n"):
        suggestion = suggestion.strip()
        if not suggestion:
            continue  # Skip empty lines
        
        if ":" in suggestion:
            title, content = suggestion.split(":", 1)
            formatted_html += (
                f"<li class='mb-2 text-gray-400'>"
                f"<span class='font-medium {suggestion_class}'>{title.strip()}:</span> {content.strip()}"
                "</li>\n"
            )
        else:
            print(f"⚠️ Skipping malformed suggestion: {suggestion}")  # Log unexpected lines

    formatted_html += "</ul>\n"
    return formatted_html
