print("\n**************************************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarters","Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["BP","Shell","Meijer","Sams Club","Marathon","Mobile","Speedway","Circle K","WaWa"]
    return random.choice(gasStationsList)

print(gasLevelGauge())
print(gasStations())