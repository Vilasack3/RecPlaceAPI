from typing import List

from pydantic import BaseModel


# Request schema for clustering-based recommendations
class ClusteringRequest(BaseModel):
    user_id: str
    top_n: int = 5


# Response schema for clustering-based recommendations
class ClusteringResponse(BaseModel):
    user_id: str
    cluster: int
    recommendations: List[str]
