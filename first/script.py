def getYear():
    while True:
        try:
            rok = int(input("Enter your birthyear: "))
            break
        except ValueError:
            print("You entered something not numeric. Try again!")
    return rok



c = 100 - (2017-getYear())

print("100 rokov sa dozijes za ",c," rokov.")