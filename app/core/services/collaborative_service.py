from typing import List

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from app.core.models.collaborative_model import CollaborativeModel


def recommend_collaborative(user_id: str, model: CollaborativeModel, interaction_matrix, top_n: int = 5) -> List[str]:
    """
    Generates recommendations for a user based on the collaborative filtering model.

    Args:
        user_id (str): User ID for whom recommendations are generated.
        model (CollaborativeModel): The collaborative filtering model.
        interaction_matrix (pandas.DataFrame): The user-item interaction matrix.
        top_n (int, optional): The number of top recommendations to return. Defaults to 5.

    Returns:
        List[str]: List of recommended items (categories).
    """

    # Ensure user_id is in interaction matrix
    if user_id not in interaction_matrix.index:
        raise ValueError(f"User ID {user_id} not found in the interaction matrix.")

    # Get user vector
    user_vector = model.get_user_vector(user_id)

    # Calculate cosine similarity between the user vector and all user vectors in the model
    similarities = cosine_similarity([user_vector], model.components_)

    # Get indices of top N similar users, excluding the user itself
    top_similar_indices = similarities.argsort()[0][-top_n - 1:-1]

    # Get items rated by top similar users
    top_similar_users = interaction_matrix.iloc[top_similar_indices]

    # Calculate recommendations
    user_ratings = interaction_matrix.loc[user_id]
    recommended_items = []

    for item_index in range(len(interaction_matrix.columns)):
        if user_ratings[item_index] == 0:  # Check for items the user hasn't rated
            similar_user_ratings = top_similar_users.iloc[:, item_index]

            # Check if there are ratings to compute a weighted average
            if np.sum(similarities[0][top_similar_indices]) > 0:
                weighted_rating = np.dot(similarities[0][top_similar_indices], similar_user_ratings) / np.sum(
                    similarities[0][top_similar_indices])
                recommended_items.append((item_index, weighted_rating))
            else:
                # If no similar ratings, avoid dividing by zero
                recommended_items.append((item_index, 0))

    # Sort recommendations by rating and return top N item names or IDs
    recommended_items.sort(key=lambda x: x[1], reverse=True)
    return [interaction_matrix.columns[i] for i, _ in recommended_items[:top_n]]
