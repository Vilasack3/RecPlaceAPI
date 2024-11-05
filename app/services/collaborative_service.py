from typing import List

import joblib

# Load the collaborative filtering model
collaborative_model = joblib.load("app/models/collaborative_model.pkl")


def get_collaborative_recommendations(user_id: str, top_n: int = 5) -> List[str]:
    """
    Generate collaborative filtering recommendations for a user.

    Parameters:
    - user_id (str): The ID of the user for whom to generate recommendations.
    - top_n (int): The number of recommendations to return.

    Returns:
    - List[str]: A list of recommended items.
    """
    try:
        # Generate recommendations using the collaborative model
        recommendations = collaborative_model.predict(user_id, top_n=top_n)
        return recommendations
    except KeyError:
        # If user is not found in the dataset, handle it gracefully
        return []
