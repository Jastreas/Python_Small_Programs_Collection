#ask for a number and just show decimal part

from pyfiglet import Figlet
from colorama import Fore

f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('Decimatron'))


correct = False
while not correct:
    try:
        numOriginal = float(input(Fore.WHITE + "Introduce a number with a decimal part\n"))
        correct = True
    except:
        print(Fore.RED + "Please introduce a correct value\n")

numNoDecimal = int(numOriginal)
print(Fore.GREEN, numOriginal-numNoDecimal)
print(Fore.WHITE + "Thanks for using!")