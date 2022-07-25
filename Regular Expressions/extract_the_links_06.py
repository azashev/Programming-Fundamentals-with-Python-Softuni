# Solution one:

import re

some_text = input()

pattern = r"(w{3}\.([a-zA-Z0-9]+\-?)+(\.[a-z]+)+)"

while some_text:
    match = re.findall(pattern, some_text)

    if match:
        print(match[0])

    some_text = input()


# Solution two:

# import re
#
# some_text = input()
#
# pattern = r"(w{3}\.([a-zA-Z0-9]+\-?)+(\.[a-z]+)+)"
# valid_urls = []
#
# while some_text:
#     match = re.search(pattern, some_text)
#
#     if match:
#         valid_urls.append(match[0])
#     some_text = input()
#
# for valid_url in valid_urls:
#     print(valid_url)


# Solution three:

# import re
#
# some_text = input()
#
# pattern = r"(w{3}\.([a-zA-Z0-9]+\-?)+(\.[a-z]+)+)"
# valid_urls = []
#
# while some_text:
#     matches = re.finditer(pattern, some_text)
#
#     for match in matches:
#         valid_urls.append(match.group(0))
#
#     some_text = input()
#
# for valid_url in valid_urls:
#     print(valid_url)


# Write a program that extracts links from a given text.
# The text will come in the form of strings, each representing a sentence.
# You need to extract only the valid links from it.

# The Sub-Domain must always be "www".
# The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–").
# The Domain extension consists of one or more domain blocks, a domain block consists of a dot followed by one or more
# lowercase English alphabet letters, a Domain extension must have at least one domain block in order to be valid.
# The Sub-Domain and Domain name must be separated by a single dot.
# Any link that does NOT follow the specified above rules should be treated as invalid.


# Example of correct links:
# • "Some textwww.softuni.bg":
# www.softuni.bg

# • "Just a link in a www.sea-of-text.bg-swimming around":
# www.sea-of-text.bg

# • "Instruments www.Instruments.rom.com.trombone2000 Instrument here":
# www.Instruments.rom.com.trombone

# • "All your ice cream flavors-www.scream.for.ice.cream(We  also have squirrels)":
# www.scream.for.ice.cream


# Example incorrect links:
# • "ww.justASite.bg"
# • "lel.awesome.com"
# • "www.weird_site.hit.bg"
# • "www.no-symb#^ols-allow%ed.com"
# • "www.mark.12"
# • "www.web-site."
# • "www.example-site._*^#"

# The output is all valid links you have found, printed – each on a new line.
