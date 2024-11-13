import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.routes.collaborative_routes import collaborative_router

# Load environment variables
load_dotenv()

# Create the FastAPI application instance
app = FastAPI()

# Include the API router
app.include_router(collaborative_router)

user_id = os.getenv('USER_ID', " User 123")
model_path = os.getenv('MODEL_PATH', "app/data/processed/collaborative_model.pkl")
