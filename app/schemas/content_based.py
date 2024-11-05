from typing import List

from pydantic import BaseModel


# Request schema for content-based recommendations
class ContentBasedRequest(BaseModel):
    user_id: str
    top_n: int = 5  # Default value for number of recommendations


# Response schema for content-based recommendations
class ContentBasedResponse(BaseModel):
    user_id: str
    recommendations: List[str]
