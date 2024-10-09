import sys
import time

# ANSI escape codes for text colors
CYAN = "\033[96m"
GREEN = "\033[92m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Resets color to default

# Print a welcome message to the user in blue
print(f"\n{BLUE}Welcome to InfoTechCenter V1.0{RESET}\n")

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