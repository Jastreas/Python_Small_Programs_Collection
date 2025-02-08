#ask for 2 numbers and calculate the division saying if its exact or not

from colorama import Fore

correct = False
while not correct:
    try:
        dividend = float(input(Fore.WHITE + "Introduce the dividend\n"))
        divisor = float(input(Fore.WHITE + "Introduce the divisor\n"))
        correct = True
    except:
        print(Fore.RED + "Please introduce a correct value\n")

if dividend%divisor == 0:
    print(Fore.GREEN, "The division is Exact, the result is:", int(dividend/divisor))
else:
    print(Fore.GREEN, "The division is Exact, the result is not:", int(dividend/divisor))

print(Fore.WHITE + "Thank's for using")