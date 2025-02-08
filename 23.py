# Ask for a number and show all the powers of 2 from 0 to that number

from pyfiglet import Figlet
from colorama import Fore

f = Figlet(font='slant')
print(Fore.CYAN, f.renderText('POWERER'))

try:
    num = int(input(Fore.WHITE + "Introduce a number: "))
    if num < 0:
        print(Fore.RED + "Please enter a non-negative number.")
        exit()
except ValueError:
    print(Fore.RED + "Please introduce a correct integer value.")
    exit()

print(Fore.CYAN + f"Powers of 2 from 0 to {num}:")

for i in range(num + 1):
    print(Fore.GREEN + f"2^{i} = {2**i}")

print(Fore.WHITE, "Thank's for using!")