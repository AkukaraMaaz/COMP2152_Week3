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

#Input combat strength for moster
mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Monster combat strength should be between 1 and 6.")
    mCombatStrength = 1 # Default value for invalid input


# Simulate Battle rounds
for j in range(1, 21, 2): # Simulation of 20 rounds stepping by 2
    # Dice rolls for hero and moster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    #Calculate the weapons
    heroWeapons = weapons[heroRoll - 1]
    monsterWeapons = weapons[monsterRoll - 1]

    #Calculate total Strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Print round details
    print(f"\nRound {j} hero rolled {heroRoll} and monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapons}, Monster selected: {monsterWeapons}.")
    print(f"Hero Total Strength: {heroTotal}, Monster Total Strength: {monsterTotal}.")

    # Determine Winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    if j == 11:
        print("\n Battle Truce declared in Round 11. Game Over!")
        break

    if j != 11:
        print("\n Battle concluded after 20 Rounds")