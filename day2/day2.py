victory_dict = {
    "scissors": "rock",
    "rock": "paper",
    "paper": "scissors",
}

lose_dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

score_dict = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

command_dict = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

response_dict = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

desired_outcome = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}
score = 0
with open('input.txt') as f:
    for line in f:
        command = line[0]
        response = line[2]
        #victory_dict
        if response == "Y":
            print("This needs to be a tie.")
            print("Opponent plays: ", command_dict[command])
            print("I play: ", command_dict[command])
            tieVal = score_dict[command_dict[command]] + 3
            print("Tie value:", tieVal)
            score = score + tieVal
            #score = score + 3
        elif response == "X":
            print("You lose!")
            loseVal = score_dict[lose_dict[command_dict[command]]] + 0
            score = score + loseVal
            print("Lose value:", loseVal)
        else:
            print("You Win!")
            winVal =  score_dict[victory_dict[command_dict[command]]] + 6
            score = score + winVal
            print("Win value:", winVal)
print(score)