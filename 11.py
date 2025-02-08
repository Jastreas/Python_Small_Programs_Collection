#Ask the user a number and show a sum
#of the natural numbers from 1 to the
#number introduced by user

userNum = (int)(input("Please introduce a Number: \n"))
res = 0
for x in range(1, userNum+1):
    res += x
print(res)