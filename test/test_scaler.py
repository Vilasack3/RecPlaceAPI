import joblib
import pandas as pd

scaler = joblib.load("app/models/scaler.pkl")

sample_data = pd.DataFrame([{
    "temple": 3.0, "resorts": 4.2, "beaches": 2.5, "parks": 3.0,
    "theatres": 4.5, "museums": 3.2, "malls": 4.1, "zoo": 2.8,
    "restaurants": 4.6, "pubs_bars": 3.5, "local_services": 2.9,
    "burger_pizza_shops": 3.1, "hotels_other_lodgings": 3.7,
    "juice_bars": 2.5, "art_galleries": 3.9, "dance_clubs": 2.7,
    "swimming_pools": 3.3, "gyms": 2.0, "bakeries": 3.8,
    "beauty_spas": 3.6, "cafes": 4.2, "view_points": 3.4,
    "monuments": 3.1, "gardens": 4.0
}])

sample_data = sample_data.astype(float)

try:
    data_scaled = scaler.transform(sample_data)
    print("Scaling successful:",data_scaled)
except Exception as e:
    print("Scaling error:",e)