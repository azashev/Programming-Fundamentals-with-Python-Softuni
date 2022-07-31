n = int(input())

heroes = {}

for _ in range(n):

    hero, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[hero] = [hp, mp]

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    hero_name = command[1]
    if command[0] == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command[0] == "Recharge":
        amount = int(command[2])
        if heroes[hero_name][1] + amount > 200:
            amount = 200 - heroes[hero_name][1]
            heroes[hero_name][1] = 200
        else:
            heroes[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == "Heal":
        amount = int(command[2])
        if heroes[hero_name][0] + amount > 100:
            amount = 100 - heroes[hero_name][0]
            heroes[hero_name][0] = 100
        else:
            heroes[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

for hero, resources in heroes.items():
    print(hero)
    print(f"  HP: {resources[0]}")
    print(f"  MP: {resources[1]}")


# Create an MMORPG game and a party of heroes.
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for
# your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by
# a single space in the following format:
# "{hero name} {HP} {MP}"
#   - HP stands for hit points and MP for mana points
#   - a hero can have a maximum of 100 HP and 200 MP
#
# After you have successfully picked your heroes, you can start playing the game.
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
#
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
#   • If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
#       - "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
#   • If the hero is unable to cast the spell print:
#       - "{hero name} does not have enough MP to cast {spell name}!"
#
# "TakeDamage – {hero name} – {damage} – {attacker}"
#   • Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#       - "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
#   • If the hero has died, remove him from your party and print:
#       - "{hero name} has been killed by {attacker}!"
#
# "Recharge – {hero name} – {amount}"
#   • The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
#     (the MP can't go over the maximum value).
#   • Print the following message:
#       - "{hero name} recharged for {amount recovered} MP!"
#
# "Heal – {hero name} – {amount}"
#   • The hero increases his HP. If a command is given that would bring the HP of the hero above the max value (100),
#     then HP is increased to 100 (the HP can't go over the maximum value).
#   • Print the following message:
#       - "{hero name} healed for {amount recovered} HP!"
#
#
# Input:
# • On the first line of the standard input, you will receive an integer n
# • On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a
#   space in the following format:
#   "{hero name} {HP} {MP}"
# • You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
#
# Output:
# • Print all members of your party who are still alive, in the following format (HP/MP need to be indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"

# Constraints:
# • The starting HP/MP of the heroes will be valid. 32-bit integers will never be negative or exceed the
#   respective limits.
# • The HP/MP amounts in the commands will never be negative.
# • The hero names in the commands will always be valid members of your party. No need to check that explicitly.
