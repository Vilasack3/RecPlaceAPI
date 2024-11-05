from typing import List

from pydantic import BaseModel


# Request schema for hybrid recommendations
class HybridRequest(BaseModel):
    user_id: str
    top_n: int = 5


# Response schema for hybrid recommendations
class HybridResponse(BaseModel):
    user_id: str
    recommendations: List[str]
