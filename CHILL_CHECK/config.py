import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'anandpandaisthegreatestofalltime')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///stress.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL_PATH = os.getenv("MODEL_PATH", "app/utils/stress_detection_model.keras")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "**")