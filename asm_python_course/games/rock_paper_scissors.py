def play_rps():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    for round in range(5):
        player_choice = input("Enter rock, paper, or scissors: ").lower().strip()
        computer_choice = random.choice(choices)

        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print(f"Final score - You: {player_score}, Computer: {computer_score}")


play_rps()
