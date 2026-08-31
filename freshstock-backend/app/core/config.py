import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FreshStock AI Backend"
    API_V1_STR: str = "/api/v1"
    
    # Using SQLite for fast hackathon prototyping
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./freshstock.db"
    
    # Twilio Settings (Placeholders for WhatsApp automation)
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID", "mock_sid")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN", "mock_token")
    TWILIO_PHONE_NUMBER: str = os.getenv("TWILIO_PHONE_NUMBER", "+1234567890")
    
    # IBM Watsonx Settings (For Granite AI)
    IBM_API_KEY: str = os.getenv("IBM_API_KEY", "mock_ibm_key")
    IBM_PROJECT_ID: str = os.getenv("IBM_PROJECT_ID", "mock_project_id")

    class Config:
        env_file = ".env"

settings = Settings()