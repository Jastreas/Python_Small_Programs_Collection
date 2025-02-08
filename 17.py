#Ask for price with vat and show it without vat

from colorama import Fore
from pyfiglet import Figlet

f = Figlet(font = 'slant')
print(f.renderText('- UNVATCALC -'))

correct = False

while correct == False:
    try:
        price = float(input(Fore.WHITE + "Introduce a Price: \n"))
        correct = True
    except:
        print(Fore.RED, "Please introduce a correct value")

print(Fore.GREEN + format(price/1.25, ".2f"))
print(Fore.WHITE, "")