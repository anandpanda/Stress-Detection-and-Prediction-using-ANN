import google.generativeai as genai
from config import Config

# Configure Gemini API
genai.configure(api_key=Config.GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def generate_stress_suggestions(stress_summary):
    """
    Generate stress management suggestions using the Gemini API.
    """
    try:
        response = gemini_model.generate_content(stress_summary)
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "<p>No suggestions generated.</p>"
    except Exception as e:
        print(f"❌ AI API Error: {str(e)}")
        return "<p>AI suggestions could not be generated. Please try again later.</p>"