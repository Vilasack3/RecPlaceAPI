# collaborative_model.py

import pandas as pd


def load_interaction_matrix(filepath: str) -> pd.DataFrame:
    """
    Load the user-item interaction matrix from a CSV file.

    Args:
        filepath (str): Path to the CSV file containing user-item interactions.

    Returns:
        pd.DataFrame: The user-item interaction matrix.
    """
    try:
        # Attempt to load the CSV with 'User' as the index column
        df = pd.read_csv(filepath)

        # Debug: Print out the first few rows to verify structure
        print("Loaded DataFrame columns:", df.columns)

        # Check if 'User' column exists and set it as index
        if 'User' not in df.columns:
            raise ValueError("The CSV file must contain a 'User' column.")

        # Set 'User' column as the index
        df.set_index("User", inplace=True)
        return df

    except Exception as e:
        raise RuntimeError(f"Failed to load interaction matrix: {str(e)}")
