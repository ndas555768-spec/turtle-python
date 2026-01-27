import random
import sys

CHOICES = ["rock", "paper", "scissors"]


def decide_winner(user: str, computer: str) -> str:
    if user == computer:
        return "tie"
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "win" if wins[user] == computer else "lose"


def play_round(user_choice: str | None = None) -> str:
    computer = random.choice(CHOICES)
    if user_choice is None:
        user = input("Enter rock, paper, or scissors (or 'quit'): ").strip().lower()
    else:
        user = user_choice

    if user in ("quit", "q"):
        return "quit"

    if user not in CHOICES:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return "invalid"

    print("Computer chose:", computer)
    result = decide_winner(user, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("🎉 You win!")
    else:
        print("😢 You lose!")
    return result


def main():
    wins = losses = ties = 0
    try:
        while True:
            res = play_round()
            if res == "quit":
                break
            if res == "win":
                wins += 1
            elif res == "lose":
                losses += 1
            elif res == "tie":
                ties += 1

            again = input("Play again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                break
    except (KeyboardInterrupt, EOFError):
        print()
        print("Exiting game.")

    print(f"Final score — Wins: {wins}, Losses: {losses}, Ties: {ties}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        # Non-interactive demo/test mode
        print("Running automated test mode...")
        random.seed(0)
        for choice in CHOICES:
            print(f"\nPlayer chooses: {choice}")
            play_round(user_choice=choice)
        print("\nAutomated test finished.")
    else:
        main()
