from pydantic import AnyHttpUrl
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "CivilCortex Agentic API"
    API_V1_STR: str = "/api"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    # AI configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

settings = Settings()
