import random

def game():
    print("you are playing the game....")
    score = random.randint(1,53)
    with open("high score.txt") as f:
        hi_score = f.read()
        if(hi_score!=""):
            hi_score = int(hi_score)
        else:
            hi_score = 0
    print(f"your score is: {score}")

    if(score>hi_score):
        with open("high score.txt", "w") as f:
            f.write(str(score))
    return score


game()