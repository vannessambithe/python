
try:
    def calculateage():
        Age = int(input("Enter your age"))
        Result =Age*12
        print(f"Your age is {Result} months")


    calculateage()

except:
    print("Not a number")