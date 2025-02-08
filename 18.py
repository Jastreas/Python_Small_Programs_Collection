# Request trip leg durations in minutes 
# (until a zero or value negative value are entered)
# and show the duration of the trip in hours and minutes

from pyfiglet import Figlet
from colorama import Fore

f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('TCALC'))

timelist = []

ask = True
while ask:

    try:
        mins = int(input(Fore.WHITE + "Please introduce an amount of minutes\n"))
        if mins > 0:
            timelist.append(mins)
        else:
            ask = False
    except:
        print(Fore.RED + "You didn't introduce a valid number\n")

totalTime = sum(timelist)

print(timelist)
h = totalTime//60
m = totalTime%60
print(Fore.GREEN + f"Total time: {h}:{m}")