# Print a decorative line for visual separation
print("\n*********************************************************\n")

# Print the title of the program
print("Weather Branch\n")

# Import necessary libraries
import random  # Used to select a random weather condition
from time import sleep  # Used to pause the program for a specified amount of time

def weather():
    """
    This function selects a random weather condition from the predefined list.

    Returns:
        str: A randomly selected weather condition.
    """
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]

    # Randomly select one weather condition from the list
    weatherCondition = random.choice(weatherForecast)

    return weatherCondition

# Get the current weather alert by calling the weather() function
weatherAlert = weather()

# Dictionary to map weather conditions to delay and speed limit
weather_responses = {
    "snowy": (30, 55),
    "blizzard": (45, 45),
    "rainy": (15, 65),
    "windy": (5, 70),
    "icy": (50, 30),
}

def vehicleResponsSystem():
    """
    This function determines the vehicle's response based on the current weather alert.
    It prints out appropriate messages and sets speed limits accordingly.
    """
    # If the weatherAlert exists in the dictionary, apply the corresponding delay and speed
    if weatherAlert in weather_responses:
        delay, speed = weather_responses[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {delay} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS has been engaged only allowing you to drive {speed}mph.")
    else:
        # Handle all other weather conditions (e.g., sunny)
        print(f"\nThe NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS has been disengaged")

# Call the vehicle response system to execute the appropriate actions based on the weather alert
vehicleResponsSystem()