def grade_func(number):
    result = None
    if 2 <= number <= 2.99:
        result = "Fail"
    elif number <= 3.49:
        result = "Poor"
    elif number <= 4.49:
        result = "Good"
    elif number <= 5.49:
        result = "Very Good"
    elif number <= 6:
        result = "Excellent"

    return result


grade = float(input())

print(grade_func(grade))
