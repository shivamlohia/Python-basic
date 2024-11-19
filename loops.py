arr = [1,2,3,4,5,6]
number1 = 6
number2 = 0

for i in arr:
    if i == number1:
        print(number1, "found")
        break
else:                                           #for loop is an if type, else runs if for is not successful
    print(number1, "not found")


for i in arr:
    if i == number2:
        print(number2, "found")
        break
else:
    print(number2, "not found")