import artwork
import random

streak = 0
print(artwork.title)
print("Welcome to High or Low!\nDo you think the next number will be higher or lower?")
print("\nThe game always starts with the number 11, get a streak of 5 to win!")
end_of_game = False

first_number = 11
while not end_of_game:


    second_number = random.randint(1, 21)

    player_input = input("\nHigher or Lower? Type H or L\n").lower()

    if player_input == "h" and second_number > first_number:
        streak += 1
        print(f"{second_number} Correct!")
        first_number = second_number
        print(f"Current Streak is: {streak}")
        print(f"\n\nThe current number is: {first_number}")
        if streak == 5:
            print("Congratulations YOU WIN!")
            end_of_game = True
    elif player_input == "l" and second_number > first_number:
        print(f"{second_number}, Unlucky")
        streak = 0
    elif player_input == "h" and second_number < first_number:
        print(f"{second_number}, Unlucky")
        streak = 0
    elif player_input == "l" and second_number < first_number:
        streak += 1
        print(f"{second_number} Correct!")
        first_number = second_number
        print(f"Current Streak is: {streak}")
        print(f"\n\nThe current number is: {first_number}")
        if streak == 5:
            print("Congratulations YOU WIN!")
            end_of_game = True