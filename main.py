import src.Game

def play():
    game = src.Game.SnakeGameAI()
    while True:
        game_over, score = game.play_step()
        if game_over == True:
            break
    


if __name__ == "__main__":
    play() # I play with myself
    # train() # AI RL play with itself
