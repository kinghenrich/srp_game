import random
print ("Welcome to my Game")
print ("Make the following selections")
print ("R for Razzor")
print ("S for Scissors")
print ("P for paper")
while True:
    user_action = input ("Enter a choice (r, p, s):")
    possible_actions = ["r" , "p" , "s"]
    computer_action = random.choice(possible_actions)
    print(f"\n Player Choice {user_action}: Computer Choice {computer_action}.\n")

    
    if user_action == "r":
        if computer_action == "s":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "p":
        if computer_action == "r":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "s":
        if computer_action == "p":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
            break
    if user_action == computer_action:
        print (f"Both players selected {user_action}. It's a tie!")
print("\nThanks for playing")