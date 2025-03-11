from app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

PORT=os.getenv("PORT", 10000)

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)