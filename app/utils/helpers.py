from typing import List


def normalize_scores(scores: List[float]) -> List[float]:
    """
    Normalize a list of scores to be between 0 and 1.

    Parameters:
    - scores (List[float]): List of scores to normalize.

    Returns:
    - List[float]: Normalized scores.
    """
    min_score = min(scores)
    max_score = max(scores)
    return [(score - min_score) / (max_score - min_score) if max_score > min_score else 0 for score in scores]
