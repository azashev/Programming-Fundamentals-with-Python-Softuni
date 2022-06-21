input_current_version = input().split(".")

current_version = ''

for i in input_current_version:
    current_version += i

current_version = int(current_version) + 1

new_version = [str(x) for x in str(current_version)]

print(*new_version, sep='.')
