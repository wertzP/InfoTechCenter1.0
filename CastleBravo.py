# Print a decorative line for visual separation
print("\n******************************************\n")

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


def vehicleResponsSystem():
    """
    This function determines the vehicle's response based on the current weather alert.
    It prints out appropriate messages and sets speed limits accordingly.
    """
    # Check the current weather alert and respond accordingly
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause for 1 second
        print("\nVRS has been engaged only allowing you to drive 55mph.")

    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "like weather conditions.")
        sleep(1)
        print("\nVRS has been engaged only allowing you to drive 45mph.")

    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS has been engaged only allowing you to drive 65mph.")

    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS has been engaged only allowing you to drive 70mph.")

    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "roads.")
        sleep(1)
        print("\nVRS has been engaged only allowing you to drive 30mph.")

    else:
        # This handles any weather condition not explicitly listed above (e.g., "sunny")
        print("\nThe NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS has been disengaged")


# Call the vehicle response system to execute the appropriate actions based on the weather alert
vehicleResponsSystem()