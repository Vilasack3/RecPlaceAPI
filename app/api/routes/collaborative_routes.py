import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.models.collaborative_model import CollaborativeModel
from app.core.services.collaborative_service import recommend_collaborative
from app.core.utils.data_utils import load_interaction_matrix

# Load environment variables
load_dotenv()

# Set up API router with a prefix
collaborative_router = APIRouter(prefix="/recommend")

# Define the model and interaction matrix paths from environment variables, or set defaults
MODEL_PATH = os.getenv("MODEL_PATH", "app/data/processed/collaborative_model.pkl")
INTERACTION_MATRIX_PATH = "app/data/raw/ratings.csv"

# Initialize the CollaborativeModel instance once with the model path
try:
    # Load interaction matrix and initialize the model with it
    interaction_matrix = load_interaction_matrix(INTERACTION_MATRIX_PATH)
    collaborative_model_instance = CollaborativeModel(MODEL_PATH, interaction_matrix=interaction_matrix)
except Exception as e:
    raise RuntimeError(f"Failed to initialize collaborative model or load interaction matrix: {str(e)}")


# Define a Pydantic model for incoming request data
class UserID(BaseModel):
    user_id: str


# Define the recommendation endpoint
@collaborative_router.post("/collaborative")
async def recommend_places(user_id: UserID):
    """
    Generates top N recommendations for a given user ID.

    Args:
        user_id (UserID): The user ID as provided in the request payload.

    Returns:
        dict: A dictionary containing recommended items for the user.
    """
    try:
        # Call the recommend_collaborative function with the user_id and model instance
        recommendations = recommend_collaborative(user_id.user_id, collaborative_model_instance, top_n=5)
    except ValueError as e:
        # Handle cases where the user ID is not found or other validation errors
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        # Handle other unexpected errors
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    return {"recommendations": recommendations}
