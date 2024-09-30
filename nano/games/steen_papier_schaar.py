import random
def start_game():
    print("Starting Rock paper scissors...")
    game_state = {"R": "rock","P": "paper","S": "scissors"}
    options = list(game_state.keys())
    winnings = ["RS", "PR", "SP"]
    result = "{0} beats {1}"

    while True:
        computer = random.choice(options)
        you = input("Choose R for rock, P for paper, S for scissors, and, done to quit the game: ").upper()

        match [you, f'{you}{computer}', computer]:
            case ["R" | "S" | "P", move, computer] if computer == you:
                print("It's a tie!\n")
            case ["R" | "S" | "P", move, computer]:
                winner, winner_move, looser_move = ("You", you, computer) if move in winnings else ("Computer", computer, you)
                print(f"{winner} won")
                print(result.format(game_state[winner_move], game_state[looser_move]),"\n")
            case ["DONE" | "END" | "STOP", _, _]:
                print("Game over!")
                break
            case [you, _, _]:
                print(f"{you} is not a valid option. Enter a valid option, please!\n")