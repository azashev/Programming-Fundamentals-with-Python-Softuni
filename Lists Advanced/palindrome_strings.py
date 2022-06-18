words = input().split()
palindrome = input()

filtered_words = [x for x in words if x == x[::-1]]
print(filtered_words)

found_palindrome = 0

for word in words:
    if palindrome == word == word[::-1]:
        found_palindrome += 1

print(f"Found palindrome {found_palindrome} times")
