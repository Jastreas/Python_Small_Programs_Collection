#ask a number and show the digits that forms it
from colorama import Fore

try:
    userNumInput = (int)(input("Introduce a number: \n"))
except:
    print(Fore.RED + "You didn't introduce any number")
    exit()

userNumInputString = str(userNumInput)
cont = 0

for char in userNumInputString:
    cont += 1

print(cont)