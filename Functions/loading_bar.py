def loading_bar(number):
    if number == 100:
        result = f"100% Complete!\n[{'%' * (number // 10)}]"
    else:
        result = f"{number}% [{('%' * (number // 10))}{('.' * (10 - (number // 10)))}]\nStill loading..."

    return result


input_number = int(input())

print(loading_bar(input_number))
