# Print separator for better output readability
print("\n**************************************************************\n")

# Indicate the Gasoline Branch section
print("Gasoline Branch\n")

# Import necessary modules
import random  # for random selection from lists and generating random numbers
from time import sleep  # for adding delays between print statements


# Function to simulate the gas level of a car
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarters", "Full Tank"]
    # Randomly select and return one gas level
    return random.choice(gasLevelList)


# Function to simulate nearby gas stations
def gasStations():
    # List of possible gas station names
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K", "WaWa"]
    # Randomly select and return one gas station
    return random.choice(gasStationsList)


# Function to alert the user based on the gas level
def gasLevelAlert():
    # Random distance to a gas station if the gas level is "Low"
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Random distance to a gas station if the gas level is "Quarter Tank"
    mileToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level
    gaslevelIndicator = gasLevelGauge()

    # Condition to check if the gas tank is "Empty"
    if gaslevelIndicator == "Empty":
        print("*** WARNING - You are on empty ***\n")
        sleep(2)  # Simulate delay
        print("Calling Triple AAA")

    # Condition to check if the gas tank is "Low"
    elif gaslevelIndicator == "Low":
        print("Your gas tank is extremely Low, checking GPS for nearest gas station\n")
        sleep(2)  # Simulate delay
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")

    # Condition to check if the gas tank is "Quarter Tank"
    elif gaslevelIndicator == "Quarter Tank":
        print("Your tank is a Quarter full, checking GPS for nearest gas station\n")
        sleep(2)  # Simulate delay
        print("The closest gas station is", gasStations(), "which is", mileToGasStationQuarterTank, "miles away.")

    # Condition to check if the gas tank is "Half Tank"
    elif gaslevelIndicator == "Half Tank":
        print("Your gas tank is half way full, which is plenty to get to your destination.")

    # Condition to check if the gas tank is "Three Quarters"
    elif gaslevelIndicator == "Three Quarters":
        print("Your gas is three quarters full, which is plenty to get to your destination.")

    # Condition for a "Full Tank"
    else:
        print("Your gas tank is full!!! Enjoy it while you can")

# Run the gas level alert function to simulate gas level and give an alert
gasLevelAlert()
