import random

# Lotto 6/49 game simulation

userNum = []        # User-selected numbers
lottoNum = []       # Lotto numbers
correctNum = []     # Correct guesses
correct = 0

# Ask user how numbers should be selected
while True:
    userChoice = input("Would you like the computer to select the numbers or you? (com/user)\n")

    # User chooses their own numbers
    if userChoice == "user":
        for _ in range(6):
            while True:
                try:
                    num = int(input("Please enter a number between 1 and 49: "))
                    if 1 <= num <= 49 and num not in userNum:
                        userNum.append(num)
                        break
                    else:
                        print("Invalid number, please try again")
                except ValueError:
                    print("Not a number, please try again")
        break

    # Computer chooses user's numbers
    elif userChoice == "com":
        for _ in range(6):
            while True:
                num = random.randint(1, 49)
                if num not in userNum:
                    userNum.append(num)
                    break
        break

    # Invalid choice
    else:
        print("Not a proper choice, please try again.\n")

# Display user's numbers (sorted)
print("Here are your numbers:", sorted(userNum))

# Generate lotto numbers
for _ in range(6):
    while True:
        number = random.randint(1, 49)
        if number not in lottoNum:
            lottoNum.append(number)
            break

# Display lotto numbers (sorted)
print("The lotto numbers are:", sorted(lottoNum))

# Check for correct guesses
for num in userNum:
    if num in lottoNum:
        correct += 1
        correctNum.append(num)

# Output results
if correct == 0:
    print(f"You guessed {correct} number(s) correctly")
else:
    print(
        f"You guessed {correct} number(s) correctly by guessing "
        f"{sorted(correctNum)}"
    )
