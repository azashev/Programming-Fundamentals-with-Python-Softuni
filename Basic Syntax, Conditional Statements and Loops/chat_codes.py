received_messages = int(input())

for message in range(received_messages):
    number = int(input())

    if number == 86:
        print("How are you?")
    elif number == 88:
        print("Hello")
    else:
        if number < 88:
            print("GREAT!")
        else:
            print("Bye.")
