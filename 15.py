# Ask for a number and show the digits inverted

from colorama import Fore

try:
    userNum = int(input("Introduce a Number: \n"))  # Input number
except ValueError:
    print(Fore.RED + "Please introduce a valid number")  # Handle invalid input
    exit()

# Convert number to string, reverse it, and store in a list
userNumCharList = list(str(userNum))[::-1]  # Original list
reversedNum = int("".join(userNumCharList))
print(reversedNum)