from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

from app.api.endpoints import collaborative

app = FastAPI()

# Load the entire pipeline (includes scaler and model)
pipeline = joblib.load("app/models/kmeans_pipeline.pkl")


app.include_router(collaborative.router, prefix="/collaborative",tags=["Collaborative Filtering"])
# Define input data model
class UserData(BaseModel):
    temple: float
    resorts: float
    beaches: float
    parks: float
    theatres: float
    museums: float
    malls: float
    zoo: float
    restaurants: float
    pubs_bars: float
    local_services: float
    burger_pizza_shops: float
    hotels_other_lodgings: float
    juice_bars: float
    art_galleries: float
    dance_clubs: float
    swimming_pools: float
    gyms: float
    bakeries: float
    beauty_spas: float
    cafes: float
    view_points: float
    monuments: float
    gardens: float

@app.post("/predict_cluster")
async def predict_cluster(user_data: UserData):
    # Convert input data to DataFrame
    data_df = pd.DataFrame([user_data.dict()])

    # Ensure data is in the correct type (float)
    data_df = data_df.astype(float)

    # Try prediction using the entire pipeline and capture any errors in detail
    try:
        # Directly predict using the pipeline, which includes scaling
        cluster = pipeline.predict(data_df)[0]
        return {"cluster": int(cluster)}
    except Exception as e:
        error_message = f"Prediction failed: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)
