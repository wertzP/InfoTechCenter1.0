print("\n**************************************************************\n")

print("Gasoline Branch\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarters","Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["BP","Shell","Meijer","Sams Club","Marathon","Mobile","Speedway","Circle K","WaWa"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    mileToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gaslevelIndicator = gasLevelGauge()
    if gaslevelIndicator == "Empty":
        print("*** WARNING - You are on empty ***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gaslevelIndicator == "Low":
        print("Your gas tank is extremely Low, checking GPS for nearest gas station\n")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gaslevelIndicator == "Quarter Tank":
        print("Your tank is a Quarter full, checking GPS for nearest gas station\n")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",mileToGasStationQuarterTank,"miles away.")
    elif gaslevelIndicator == "Half Tank":
        print("Your gas tank is half way full, which is plenty to get to your destination.")
    elif gaslevelIndicator == "Three Quarters":
        print("Your gas is three quarters full, which is plenty to get to your destination.")
    else:
        print("Your gas tank is full!!! Enjoy it while you can")



gasLevelAlert()