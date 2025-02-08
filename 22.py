#ask for a base and an exponent and calculate the result

from colorama import Fore

correct = False
while not correct:
    try:
        base = int(input(Fore.WHITE + "Introduce the base\n"))
        exponent = int(input(Fore.WHITE + "Introduce the exponent\n"))
        correct = True
    except ValueError:
        print(Fore.RED + "Please introduce a correct value\n")

res = base ** exponent

print(Fore.GREEN, res)
print(Fore.WHITE, "Thank's for using!")