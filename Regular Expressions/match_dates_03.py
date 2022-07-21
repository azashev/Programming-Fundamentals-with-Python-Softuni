# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.

# Every valid date has the following characteristics:
# • It always starts with two digits, followed by a separator
# • After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar)
# • After that, it has a separator and exactly 4 digits (for the year)
# • The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/")
# • The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT)
#   Use a group backreference to check for this

import re

some_text = input()

pattern = r"(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

matches = re.finditer(pattern, some_text)

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")
