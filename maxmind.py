from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError


# Function to get location data from latitude and longitude using Nominatim
def get_location_from_coordinates(latitude, longitude):
    # Set a valid user-agent to prevent the 403 error
    geolocator = Nominatim(user_agent="my_geolocation_app")

    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location:
            return location.address
        else:
            return "Location not found"
    except GeocoderServiceError as e:
        return f"Geocoding service error: {e}"


# Example usage
if __name__ == "__main__":
    latitude = 37.7749  # Example: Latitude for San Francisco, CA
    longitude = -122.4194  # Example: Longitude for San Francisco, CA

    # Get detailed location information from latitude and longitude
    address = get_location_from_coordinates(latitude, longitude)
    print(f"Location Address: {address}")
