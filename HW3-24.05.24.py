def square(symbol, lenght, void):
    print(symbol*lenght)
    for i in range(lenght-1):
        if void:
            middle = ""*(lenght-2)
        else:
            middle = symbol*(lenght-2)
        print(f"{symbol}{middle}{symbol}")
    print(symbol * lenght)
square('+', 5, True)