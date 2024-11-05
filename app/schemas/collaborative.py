from pydantic import BaseModel

class CollaborativeRequest(BaseModel):
    user_id: str
    top_n: int = 5  # Optional, default to top 5 recommendations
