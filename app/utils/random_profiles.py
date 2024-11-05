import random
import pandas as pd
import os

directory = "data"
file_name = "random_profiles.csv"

if not os.path.exists(directory):
    os.makedirs(directory)

    file_path = os.path.join(directory, file_name)

def generate_random_profile():
    return {
        "temple": round(random.uniform(1.0, 5.0), 1),
        "resorts": round(random.uniform(1.0, 5.0), 1),
        "beaches": round(random.uniform(1.0, 5.0), 1),
        "parks": round(random.uniform(1.0, 5.0), 1),
        "theatres": round(random.uniform(1.0, 5.0), 1),
        "museums": round(random.uniform(1.0, 5.0), 1),
        "malls": round(random.uniform(1.0, 5.0), 1),
        "zoo": round(random.uniform(1.0, 5.0), 1),
        "restaurants": round(random.uniform(1.0, 5.0), 1),
        "pubs_bars": round(random.uniform(1.0, 5.0), 1),
        "local_services": round(random.uniform(1.0, 5.0), 1),
        "burger_pizza_shops": round(random.uniform(1.0, 5.0), 1),
        "hotels_other_lodgings": round(random.uniform(1.0, 5.0), 1),
        "juice_bars": round(random.uniform(1.0, 5.0), 1),
        "art_galleries": round(random.uniform(1.0, 5.0), 1),
        "dance_clubs": round(random.uniform(1.0, 5.0), 1),
        "swimming_pools": round(random.uniform(1.0, 5.0), 1),
        "gyms": round(random.uniform(1.0, 5.0), 1),
        "bakeries": round(random.uniform(1.0, 5.0), 1),
        "beauty_spas": round(random.uniform(1.0, 5.0), 1),
        "cafes": round(random.uniform(1.0, 5.0), 1),
        "view_points": round(random.uniform(1.0, 5.0), 1),
        "monuments": round(random.uniform(1.0, 5.0), 1),
        "gardens": round(random.uniform(1.0, 5.0), 1)
    }
num_profiles = 1
random_profiles = [generate_random_profile() for _ in range(num_profiles)]

df_random_profiles = pd.DataFrame(random_profiles)

df_random_profiles.to_csv(file_name, index=False)
print(df_random_profiles.head())