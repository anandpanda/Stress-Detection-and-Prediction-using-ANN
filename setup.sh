#!/bin/bash

echo "🚀 Setting up Chill Check..."

# Step 1: Create & activate a virtual environment
echo -e "\n\n📦 Creating virtual environment..."
python3.11 -m venv venv
source venv/Scripts/activate
# venv\Scripts\activate    # On Windows (uncomment for Windows)

# Step 2: Install dependencies
echo -e "\n\n📦 Installing dependencies..."
pip install --no-cache-dir -r requirements.txt

# Step 3: Apply database migrations
echo -e "\n\n📊 Applying database migrations..."
cd CHILL_CHECK
flask db upgrade

# Step 4: Run the Flask app
echo -e "\n\n✅ Setup complete! Starting the application..."
flask run