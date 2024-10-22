# Print separator for better output readability
print("\n**************************************************************\n")

# Indicate the Gasoline Branch section
print("Gasoline Branch\n")

import random
from time import sleep

# Function to simulate the gas level of a car
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarters", "Full Tank"]
    return random.choice(gasLevelList)

# Function to simulate nearby gas stations
def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K", "WaWa"]
    return random.choice(gasStationsList)

# Function to simulate distance to a gas station based on gas level
def getDistance(gas_level):
    if gas_level == "Low":
        return round(random.uniform(1, 25), 1)
    elif gas_level == "Quarter Tank":
        return round(random.uniform(25.1, 50), 1)
    return None  # No need for distance for other gas levels

# Function to alert the user based on the gas level
def gasLevelAlert():
    gaslevelIndicator = gasLevelGauge()  # Get the current gas level
    print(f"\nGas Level: {gaslevelIndicator}\n")  # Display current gas level

    # Mapping gas levels to actions
    alerts = {
        "Empty": "*** WARNING - You are on empty ***\n\nCalling Triple AAA",
        "Low": f"Your gas tank is extremely Low. The closest gas station is {gasStations()} which is {getDistance('Low')} miles away.",
        "Quarter Tank": f"Your tank is a Quarter full. The closest gas station is {gasStations()} which is {getDistance('Quarter Tank')} miles away.",
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarters": "Your gas is three quarters full, which is plenty to get to your destination.",
        "Full Tank": "Your gas tank is full! Enjoy the ride."
    }

    # Print alert based on gas level
    if gaslevelIndicator in alerts:
        print(alerts[gaslevelIndicator])

    # Simulate a delay if gas is Low or Quarter Tank
    if gaslevelIndicator in ["Low", "Quarter Tank"]:
        sleep(2)

# Run the gas level alert function
gasLevelAlert()
