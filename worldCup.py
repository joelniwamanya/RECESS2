import random
#team stats
morale = 70
strength = 70
injuries = 0
points = 0


# PLACEHOLDER FUNCTIONS

def substitute_player():
    # Future substitution feature
    pass

def check_var_decision():
    # Future VAR feature
    pass



print(" 2026 FIFA WORLD CUP MANAGER")



# PRE-TOURNAMENT PREPARATION

print("\nPRE-TOURNAMENT PREPARATION")

for day in range(1, 4):

    print(f"\nDay {day}")
    print("1. Train Hard")
    print("2. Friendly Match")
    print("3. Rest / Recovery")

    choice = input("Choose an activity (1-3): ").strip()

    if choice == "1":
        strength += 5
        morale -= 2

        # Injury risk during training
        if random.randint(1, 100) <= 15:
            injuries += 1
            print("A player got injured during training!")

        print("Training increased strength.")

    elif choice == "2":
        strength += 3
        morale += 5
        print("Friendly match boosted morale and strength.")

    elif choice == "3":
        morale += 8
        print("Players recovered and morale improved.")

    else:
        print("Invalid choice. Skipping this day.")
        continue

    # Keep stats realistic
    morale = max(0, min(100, morale))
    strength = max(0, min(100, strength))

    print("\nCurrent Team Status")
    print(f"Morale: {morale}")
    print(f"Strength: {strength}")
    print(f"Injuries: {injuries}")


# GROUP STAGE

print("GROUP STAGE")

for match in range(1, 4):

    print(f"\nGROUP MATCH {match}")

    if injuries >= 3:
        print("Too many injuries!")
        print("Your weakened squad automatically loses.")
        continue

    print("1. Attacking Formation")
    print("2. Defensive Formation")
    print("3. Balanced Formation")

    choice = input("Choose your tactic (1-3): ").strip()

    if choice == "1":
        strength -= 3
        result_chance = strength + morale

    elif choice == "2":
        morale -= 2
        result_chance = strength + morale + 10

    elif choice == "3":
        result_chance = strength + morale + 5

    else:
        print("Invalid tactic.")
        result_chance = strength + morale - 15

    # Random match factor
    result_chance += random.randint(-20, 20)

    # Match result
    if result_chance >= 160:
        print("RESULT: WIN")
        points += 3
        morale += 5

    elif result_chance >= 130:
        print("RESULT: DRAW")
        points += 1

    else:
        print("RESULT: LOSS")

    # Injury chance
    if random.randint(1, 100) <= 20:
        injuries += 1
        print("A player suffered an injury.")

    substitute_player()
    check_var_decision()

    morale = max(0, min(100, morale))
    strength = max(0, min(100, strength))

    print("\nCurrent Team Status")
    print(f"Morale: {morale}")
    print(f"Strength: {strength}")
    print(f"Injuries: {injuries}")
    print(f"Points: {points}")


# GROUP STANDINGS


print("GROUP STAGE COMPLETE")


# Simulate the other teams
team_b = random.randint(0, 9)
team_c = random.randint(0, 9)
team_d = random.randint(0, 9)

standings = [
    ("Your Team", points),
    ("Team B", team_b),
    ("Team C", team_c),
    ("Team D", team_d)
]

# Sort by points (highest first)
standings.sort(key=lambda team: team[1], reverse=True)

print("\nFINAL GROUP STANDINGS")

for position, team in enumerate(standings, start=1):
    print(f"{position}. {team[0]} - {team[1]} points")

# Determine your position
for position, team in enumerate(standings, start=1):
    if team[0] == "Your Team":
        your_position = position
        break

if your_position <= 2:
    print("\nYou finished in the TOP TWO.")
    print("Congratulations! You qualify for the Knockout Stage.")
    qualified = True
else:
    print("\nYou finished outside the top two.")
    print("Your World Cup journey ends here.")
    qualified = False

# KNOCKOUT STAGE

rounds = [
    "Round of 16",
    "Quarter-final",
    "Semi-final",
    "Final"
]

if qualified:

    print("KNOCKOUT STAGE")

    for stage in rounds:

        print(f"\n{stage}")

        if injuries >= 4:
            print("Too many injuries!")
            print("Your team cannot continue.")
            break

        print("1. Attacking Formation")
        print("2. Defensive Formation")
        print("3. Balanced Formation")

        choice = input("Choose your tactic (1-3): ").strip()

        if choice == "1":
            strength -= 3
            result_chance = strength + morale

        elif choice == "2":
            morale -= 2
            result_chance = strength + morale + 10

        elif choice == "3":
            result_chance = strength + morale + 5

        else:
            print("Invalid tactic.")
            result_chance = strength + morale - 15

        result_chance += random.randint(-15, 15)

        if result_chance >= 150:

            print(f"You WON the {stage}!")
            morale += 5

            if random.randint(1, 100) <= 15:
                injuries += 1
                print("A player picked up an injury.")

            if stage == "Semi-final":
                print("\nYou have reached the FIFA World Cup Final!")

            if stage == "Final":
                print("\n🏆🏆🏆 WORLD CUP CHAMPIONS 🏆🏆🏆")
                print("CONGRATULATIONS!")
                print("YOU WON THE 2026 FIFA WORLD CUP!")
                break

        else:

            if stage == "Semi-final":
                print("You lost the Semi-final.")
                print("You will now play for Third Place.")

                third_place_result = strength + morale + random.randint(-15, 15)

                print("\nTHIRD PLACE PLAYOFF")

                if third_place_result >= 140:
                    print("You won the Third Place Match!")
                    print("🥉 Your team finishes THIRD in the World Cup.")
                else:
                    print("You lost the Third Place Match.")
                    print("Your team finishes FOURTH.")

                break

            else:
                print(f"You LOST the {stage}.")
                print("Tournament Over.")
                break


# TOURNAMENT SUMMARY
print("TOURNAMENT SUMMARY")

print(f"Final Morale: {morale}")
print(f"Final Strength: {strength}")
print(f"Total Injuries: {injuries}")
print(f"Group Stage Points: {points}")

if qualified:
    print(f"Group Position: {your_position}")
else:
    print("Eliminated in Group Stage")

print("\nThank you for managing your national team!")