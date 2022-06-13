def perfect_number(number):
    sum_divisors = 0
    for x in range(1, number):
        if number % x == 0:
            sum_divisors += x

    if number == sum_divisors:
        return True

    return False


input_number = int(input())
print()
if perfect_number(input_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
