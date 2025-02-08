#ask for 2 numbers to user and show the sum from all the natural numbres between them

res = 0
n1 = (int)(input("Please introduce the first number \n"))
n2 = (int)(input("Please introduce the second number \n"))

def Compare(nu1, nu2):
    return min(nu1, nu2)

if Compare(n1,n2) == n1:
    for x in range(n1, n2+1):
        res += x
else:
    for x in range(n2, n1+1):
        res += x

print(res)