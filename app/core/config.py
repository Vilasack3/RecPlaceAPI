from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # General application settings
    app_name: str = "Recommendation System API"
    debug: bool = Field(default=False, env="DEBUG")
    version: str = "1.0.0"

    # Server settings
    host: str = Field(default="127.0.0.1", env="HOST")
    port: int = Field(default=8000, env="PORT")

    # Model paths
    model_path: str = Field(default="app/models/", env="MODEL_PATH")
    collaborative_model: str = Field(default="collaborative_model.pkl", env="COLLABORATIVE_MODEL")
    content_based_model: str = Field(default="content_based_model.pkl", env="CONTENT_BASED_MODEL")
    clustering_model: str = Field(default="clustering_model.pkl", env="CLUSTERING_MODEL")

    # Database settings (optional)
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_name: str = Field(default="recommendation_db", env="DB_NAME")
    db_user: str = Field(default="db_user", env="DB_USER")
    db_password: str = Field(default="supersecretpassword", env="DB_PASSWORD")

    # API keys or secret keys
    api_key: str = Field(default="your_api_key_here", env="API_KEY")
    secret_key: str = Field(default="your_secret_key_here", env="SECRET_KEY")

    # Logging settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    class Config:
        # Load environment variables from a .env file if it exists
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Instantiate the settings, so we can import this in other parts of the app
settings = Settings()
