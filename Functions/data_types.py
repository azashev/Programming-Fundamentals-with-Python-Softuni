# def type_int(int_number):
#     return int_number * 2
#
#
# def type_float(float_number):
#     result = float_number * 1.5
#     return f"{result:.2f}"
#
#
# def type_string(string):
#     return "$" + string + "$"
#
#
# data_type = input()
# value = input()
#
# if data_type == "int":
#     value = int(value)
#     print(type_int(value))
# elif data_type == "real":
#     value = float(value)
#     print(type_float(value))
# elif data_type == "string":
#     print(type_string(value))


def calculations(data_type, value):
    if data_type == "int":
        value = int(value)
        return value * 2

    if data_type == "real":
        value = float(value)
        return f"{value * 1.5:.2f}"

    if data_type == "string":
        return "$" + value + "$"


input_data_type = input()
input_value = input()

print(calculations(input_data_type, input_value))
