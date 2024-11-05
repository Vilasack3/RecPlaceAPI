from typing import List

from app.services.collaborative_service import get_collaborative_recommendations
from app.services.content_based_service import get_content_based_recommendations


def get_hybrid_recommendations(user_id: str, top_n: int = 5, weight_collab: float = 0.5, weight_content: float = 0.5) -> \
        List[str]:
    """
    Generate hybrid recommendations using collaborative and content-based filtering.

    Parameters:
    - user_id (str): The ID of the user for whom to generate recommendations.
    - top_n (int): The number of recommendations to return.
    - weight_collab (float): Weight for collaborative filtering.
    - weight_content (float): Weight for content-based filtering.

    Returns:
    - List[str]: A list of recommended items based on hybrid filtering.
    """
    # Get recommendations from both collaborative and content-based services
    collab_recommendations = get_collaborative_recommendations(user_id, top_n=top_n)
    content_recommendations = get_content_based_recommendations(user_id, top_n=top_n)

    # Combine and rank recommendations based on weights
    combined_recommendations = list(set(collab_recommendations + content_recommendations))

    # For simplicity, just merge and truncate. In production, you could refine this.
    return combined_recommendations[:top_n]
