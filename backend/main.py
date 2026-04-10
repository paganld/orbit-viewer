from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio

from services.data_fetcher import DataFetcher

# Create a global instance of the DataFetcher
data_fetcher = DataFetcher()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the background data fetching task
    print("Starting background data fetcher...")
    fetch_task = asyncio.create_task(data_fetcher.run_periodic_fetch())
    yield
    # Clean up the task on shutdown
    print("Stopping background data fetcher...")
    fetch_task.cancel()
    try:
        await fetch_task
    except asyncio.CancelledError:
        print("Background task cancelled successfully.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Orbitviewer Backend is running."}

@app.get("/api/v1/flights")
async def get_flights():
    # Placeholder for flight data
    return data_fetcher.get_data("flights")

@app.get("/api/v1/ships")
async def get_ships():
    # Placeholder for ship data
    return data_fetcher.get_data("ships")

# We will add more endpoints for satellites, news, etc.
