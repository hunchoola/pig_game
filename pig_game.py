import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if players > 1 and players <= 4:
            break
        else:
            print("Must be between 2 - 4 players. ")

max_score = 20
player_scores = [0 for i in range(players)]


while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx])
        current_score = 0

        while True:

            roll_option = input("Would you like to roll (y)/(n)?")
            if roll_option.lower() == "y":
                value = roll()
            else:
                break
            if value == 1:
                print("you rolled a 1! Turn done!")
                current_score = 0
            else:
                current_score += value
                print("You roll a: ", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])


max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player number", winner + 1, "is the winner with a score of:", max_score)
# print(f"Player number" {winner} + 1 "is the winner with a score of:" {max_score})
