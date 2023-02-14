num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

for i in range(num1,num2):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"Fizzbuzz")
    elif i % 5 == 0:
        print(i,"Fizz")
    elif i % 3 == 0:
        print(i,"Buzz")