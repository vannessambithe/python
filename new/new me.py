for number in range(1,100):
    if number % 3 == 0 and number % 5 == 0:
        print(number,"fizzbuzz")

    elif number % 3 == 0:
        print(number,"fizz")

    elif number % 5 == 0:
        print(number,"buzz")

