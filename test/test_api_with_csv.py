from pprint import pprint

import pandas as pd
import requests

file_path = "data/random_profiles.csv"
df = pd.read_csv(file_path)

url = "http://127.0.0.1:8000/predict_cluster"

for index, row in df.iterrows():
    data = row.to_dict()

    response = requests.post(url, json=data)

    if response.status_code == 200:
        pprint(f"Row {index} - Cluster: {response.json()}")
    else:
        pprint(f"Row {index} - Failed with status code: {response.status_code}")
        pprint(f"Error: {response.json()}")
