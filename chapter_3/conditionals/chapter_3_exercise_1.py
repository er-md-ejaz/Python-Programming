winning_number = 45
user_input = input("Guess number between 1 to 100: ")
user_input = int(user_input)
if user_input == winning_number:
    print("you win")
else:
    if user_input > winning_number:
        print("too high")
    else:
        print("too low")