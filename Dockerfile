# Use an official lightweight Python image
FROM python:3.9
LABEL authors="z"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["gunicorn", "-w", "4", "-k","uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "127.0.0.1:8000"]

