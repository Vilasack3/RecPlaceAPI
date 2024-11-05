from fastapi import APIRouter, HTTPException
from app.schemas.collaborative import CollaborativeRequest
from app.services.collaborative_service import get_collaborative_recommendations

router = APIRouter()

@router.post("/recommend", summary="Get collaborative filtering recommendations")
async def collaborative_recommend(request: CollaborativeRequest):
    try:
        recommendations = get_collaborative_recommendations(request.user_id)
        return {"user_id": request.user_id, "recommendations": recommendations}
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")
