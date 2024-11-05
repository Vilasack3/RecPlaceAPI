from typing import List

import joblib
import pandas as pd

# Load the clustering model and data
clustering_model = joblib.load("app/models/clustering_model.pkl")
cluster_profiles = pd.read_csv("data/item_profiles.csv")  # Example of cluster-based recommendations


def get_cluster_recommendations(user_id: str, top_n: int = 5) -> List[str]:
    """
    Generate recommendations based on the user's assigned cluster.

    Parameters:
    - user_id (str): The ID of the user for whom to generate recommendations.
    - top_n (int): The number of recommendations to return.

    Returns:
    - List[str]: A list of recommended items based on the user's cluster.
    """
    try:
        # Determine the user's cluster
        user_cluster = clustering_model.predict([user_id])[0]

        # Retrieve recommendations for the cluster
        cluster_recommendations = cluster_profiles.loc[user_cluster, "recommendations"].split(',')
        return cluster_recommendations[:top_n]
    except KeyError:
        # If the user or cluster is not found, return an empty list
        return []
