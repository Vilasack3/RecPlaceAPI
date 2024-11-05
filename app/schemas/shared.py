from typing import List

from pydantic import BaseModel


# Shared schema for a user ID
class UserID(BaseModel):
    user_id: str


# Shared schema for a recommendation response
class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[str]
