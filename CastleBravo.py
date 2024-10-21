import sys
import time

# ANSI escape codes for text colors
CYAN = "\033[96m"
GREEN = "\033[92m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets color to default

# Print a welcome message to the user in blue
print(f"\n{BLUE}Welcome to InfoTechCenter V1.0{RESET}\n")

timeToSleep = 2.5  # Variable to set the time library to 2.5 seconds when called
time.sleep(timeToSleep)  #Calling the time to sleep with the variable with the value timeToSleep

x = 0  # Counter variable for loop iterations
ellipsis = 0  # Counter for the number of dots in the boot message

# Loop that runs 20 times to simulate the system booting process
while x != 20:
    x += 1  # Increment the loop counter
    # Create the boot message in cyan with a dynamic number of dots (based on ellipsis)
    message = (f"{CYAN}InfoTech Center System Booting{RESET}" + "." * ellipsis)

    # Increment the ellipsis to add more dots on the next iteration
    ellipsis += 1

    # Overwrite the current line in the terminal with the new message
    sys.stdout.write("\r" + message)

    # Pause for half a second to simulate a delay in the booting process
    time.sleep(.5)

    # Reset ellipsis to 0 after reaching 3 dots (so it cycles between 0 to 3 dots)
    if ellipsis == 4:
        ellipsis = 0

    # Once the loop runs 20 times, print the final message and exit the loop
    if x == 20:
        print(f"\n\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")

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