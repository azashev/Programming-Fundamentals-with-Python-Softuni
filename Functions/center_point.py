from math import floor


def closest_points(x1, y1, x2, y2):
    closest_x, closest_y = None, None

    if abs(x1) <= abs(x2):
        closest_x = x1
    else:
        closest_x = x2

    if abs(y1) <= abs(y2):
        closest_y = y1
    else:
        closest_y = y2

    return closest_x, closest_y


input_x1 = float(input())
input_x2 = float(input())

input_y1 = float(input())
input_y2 = float(input())


final_x, final_y = closest_points(input_x1, input_x2, input_y1, input_y2)


print(f"({floor(final_x)}, {floor(final_y)})")
