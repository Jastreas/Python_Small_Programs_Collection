#ask a price and show the price + VAT

from colorama import Fore
from pyfiglet import Figlet

f = Figlet(font = 'slant')
print(f.renderText('VATCALC'))

try:
    price = float(input("Please Introduce the price: \n"))
except:
    print(Fore.RED + "Please introduce a proper value.")
    exit()

res = price + (price * 0.25) #price + vat
res = format(res,".2f") #2 decimals

print(Fore.GREEN + res, "€")

print(Fore.WHITE + "Thanks for using!")