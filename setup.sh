#!/bin/bash

# Script to set up the Flask app

# Step 1: Create a virtual environment
echo "\n\Creating a virtual environment..."
python3.11 -m venv venv

# Step 2: Activate the virtual environment
echo "\n\nActivating the virtual environment..."
source venv/Scripts/activate  # On macOS/Linux
# venv\Scripts\activate    # On Windows (uncomment for Windows)

# Step 3: Install dependencies
echo "\n\nInstalling dependencies..."
pip install -r requirements.txt

# Step 4: Set up the database
echo "\n\nSetting up the database..."
cd CHIILL_CHECK
flask db upgrade

# Step 5: Run the app
echo "\n\nThe app has been set up."
flask run