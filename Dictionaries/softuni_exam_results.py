results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split("-")
    username = command[0]

    if command[1] == "banned":
        for lang, users in results.items():
            for user in users:
                if user == username:
                    del results[lang][user]
                    break
    else:
        language = command[1]
        points = int(command[2])

        if language not in results:
            results[language] = {}
            results[language][username] = points

        else:
            if username not in results[language]:
                results[language][username] = points
            else:
                if results[language][username] < points:
                    results[language][username] = points

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for language, usernames in results.items():
    for user, points in usernames.items():
        print(f"{user} | {points}")
print("Submissions:")
for language, score in submissions.items():
    print(f"{language} - {score}")


# Judge statistics on the last Programing Fundamentals exam were not working correctly, so all the submissions must be
# analyzed properly. Collect all the submissions and print the final results and statistics about each language in which
# participants submitted their solutions.

# You will be receiving lines in the following format:
# "{username}-{language}-{points}" until you receive "exam finished".
# Store each username, their submissions and points. If a student has two or more submissions for the same language,
# save only his maximum points.

# You can receive a command to ban a user for cheating in the following format:
# "{username}-banned".
# In that case, you remove the user from the contest but preserve his submissions in the total count of submissions for
# each language.

# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"

# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"


# Input / Constraints:
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}"

# You can receive a ban command -> "{username}-banned"

# The points of the participant will always be a valid integer in the range [0-100];

# Output:
# •	Print the exam results for each participant
# •	After that, print each language in the format shown above
# •	Allowed working time / memory: 100ms / 16MB
