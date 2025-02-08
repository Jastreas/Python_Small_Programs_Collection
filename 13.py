#ask a number to the user and show all the multiples from 0 to 100

userNum = (int)(input("Please introduce a whole number: "))

# Generate and print multiples from 0 to 100
print(f"Multiples of {userNum} from 0 to 100:")
for i in range(101):
    if i % userNum == 0:
        print(i)