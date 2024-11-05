from typing import List

import joblib

# Load the content-based filtering model
content_based_model = joblib.load("app/models/content_based_model.pkl")


def get_content_based_recommendations(user_id: str, top_n: int = 5) -> List[str]:
    """
    Generate content-based recommendations for a user.

    Parameters:
    - user_id (str): The ID of the user for whom to generate recommendations.
    - top_n (int): The number of recommendations to return.

    Returns:
    - List[str]: A list of recommended items based on content similarity.
    """
    try:
        # Generate recommendations using the content-based model
        recommendations = content_based_model.predict(user_id, top_n=top_n)
        return recommendations
    except KeyError:
        # If user or content data is not found, return an empty list
        return []
