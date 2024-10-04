from fastapi import FastAPI
import redis
import requests
import json

app = FastAPI()

redis_password = '*************'

# Redis connection details
redis_host = "**************"
redis_port = *****

# Connect to Redis database
redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=0)

@app.get("/weather/{city}")
async def get_weather(city: str):
    # Fetch weather data from a weather API 
    # Replace with your API key and URL
    api_key = "***********************"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make API request and handle response
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch weather data. Please try again later."}

    # Cache weather data in Redis
    redis_client.set(city, json.dumps(data),ex=3600)

    return data