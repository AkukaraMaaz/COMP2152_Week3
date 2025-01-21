import random

# Dice Options using list() and range()
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']


print("Available Weapons:", ', '.join(weapons))

# Inputs combat strength here
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1 # Default value for invalid input

# combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
# mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))
#
# # Battle
# for j in range(1, 21, 2):
#     heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
#     heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
#     print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.",
#           "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
#     if j == 11:
#         print("Battle Truce declared. Game Over!")
#         break