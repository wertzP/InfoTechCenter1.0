print("\n******************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponsSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forcast of", weatherAlert, "weather conditions.")

vehicleResponsSystem()