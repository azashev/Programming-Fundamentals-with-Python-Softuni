def has_20_characters(ticket):
    return len(ticket) == 20


def is_winning_jackpot(ticket):
    symbols = ["@", "#", "$", "^"]
    if has_20_characters(ticket):
        ticket_left_side = ticket[:10]
        ticket_right_side = ticket[10:]

        match_counter_left = 0
        uninterrupted_repeats_left = 0
        for char in ticket_left_side:
            if char in symbols:
                match_counter_left += 1
                if match_counter_left > uninterrupted_repeats_left:
                    uninterrupted_repeats_left = match_counter_left
                symbols = char
            else:
                match_counter_left = 0

        match_counter_right = 0
        uninterrupted_repeats_right = 0
        for char in ticket_right_side:
            if char == symbols:
                match_counter_right += 1
                if match_counter_right > uninterrupted_repeats_right:
                    uninterrupted_repeats_right = match_counter_right
            else:
                match_counter_right = 0

        if uninterrupted_repeats_left > uninterrupted_repeats_right:
            counter = uninterrupted_repeats_right
        elif uninterrupted_repeats_right > uninterrupted_repeats_left:
            counter = uninterrupted_repeats_left
        else:
            counter = uninterrupted_repeats_left

        if counter < 6:
            return f'ticket "{ticket}" - no match'
        elif counter < 10:
            return f'ticket "{ticket}" - {counter}{symbols}'
        elif counter >= 10:
            return f'ticket "{ticket}" - {counter}{symbols} Jackpot!'
    else:
        return f"invalid ticket"


tickets = [x.strip() for x in input().split(", ")]

for ticket in tickets:
    print(is_winning_jackpot(ticket))


# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# • A valid ticket has exactly 20 characters.
# • A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at
# least 6 times in both halves of the tickets.
# • In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides

# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"

# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"


# Input:
# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:
# • "{ticket}, {ticket}, … {ticket}"


# Output:
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# • If the ticket is invalid:
# "invalid ticket"

# • If the ticket is valid, but it is not winning:
# "ticket "{ticket}" - no match"

# • If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"

# • If the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"


# Constrains:
# • Number of tickets will be in range [0 … 100]
