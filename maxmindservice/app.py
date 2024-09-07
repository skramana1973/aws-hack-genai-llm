from fastapi import FastAPI
from maxmindservice.maxmind import get_location_from_coordinates

# Create the FastAPI app
app = FastAPI()


# Define a root route ("/") that returns a simple welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI service!"}


# Define a route with a parameter to greet a user by name
@app.get("/greet")
def greet_user(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}


# Define a route that accepts two numbers and returns their sum
@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}


# Example route for providing location info (inspired by geocoding example)
@app.get("/location")
def get_location(lat: float, lon: float):
    return {"Location": f"{get_location_from_coordinates(lat, lon)}"}
