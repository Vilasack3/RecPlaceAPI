# collaborative_model.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class CollaborativeModel:
    def __init__(self, interaction_matrix: pd.DataFrame):
        """
        Initialize the CollaborativeModel with a given interaction matrix.

        Args:
            interaction_matrix (pd.DataFrame): A DataFrame where rows represent users,
                                               columns represent items, and values represent ratings.
        """
        self.interaction_matrix = interaction_matrix
        self.similarity_matrix = None

    def compute_similarity(self):
        """
        Compute the similarity between users based on the interaction matrix
        using cosine similarity.
        """
        self.similarity_matrix = pd.DataFrame(
            cosine_similarity(self.interaction_matrix),
            index=self.interaction_matrix.index,
            columns=self.interaction_matrix.index
        )
        print("User similarity matrix computed.")

    def get_recommendations(self, user_id: str, top_n: int = 5):
        """
        Get recommendations for a specific user based on collaborative filtering.

        Args:
            user_id (str): The ID of the user for whom to generate recommendations.
            top_n (int): The number of top recommendations to return.

        Returns:
            pd.Series: A Series of item recommendations with item names as index and
                       predicted ratings as values, sorted in descending order.
        """
        # Ensure the similarity matrix is computed
        if self.similarity_matrix is None:
            self.compute_similarity()

        if user_id not in self.similarity_matrix.index:
            raise ValueError(f"User ID '{user_id}' not found in interaction matrix.")

        # Get the most similar users to the specified user
        similar_users = self.similarity_matrix[user_id].sort_values(ascending=False).iloc[1:top_n + 1]

        # Weighted average of ratings by similar users
        weighted_ratings = self.interaction_matrix.loc[similar_users.index].T.dot(similar_users)
        recommendation_scores = weighted_ratings / similar_users.sum()

        # Filter out items already rated by the user
        user_rated_items = self.interaction_matrix.loc[user_id]
        recommendations = recommendation_scores[user_rated_items == 0]

        return recommendations.sort_values(ascending=False).head(top_n)


# Utility function to load the interaction matrix
def load_interaction_matrix(filepath: str) -> pd.DataFrame:
    """
    Load the user-item interaction matrix from a CSV file.

    Args:
        filepath (str): Path to the CSV file containing user-item interactions.

    Returns:
        pd.DataFrame: The user-item interaction matrix.
    """
    try:
        # Load the CSV with 'User' as the index column
        df = pd.read_csv(filepath, index_col="User")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load interaction matrix: {str(e)}")
