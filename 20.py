#ask for a number and show just the whole part

from pyfiglet import Figlet
from colorama import Fore

f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('WHOLEME'))
numUser = float(input(Fore.WHITE + "Introduce a number\n"))
print(Fore.GREEN, int(numUser))