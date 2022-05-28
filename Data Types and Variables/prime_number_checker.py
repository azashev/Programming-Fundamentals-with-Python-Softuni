number = int(input())

if number > 0:
    if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
        print(True)
    else:
        if number % 2 == 0:
            print(False)
        else:
            if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
                print(False)
            else:
                print(True)
