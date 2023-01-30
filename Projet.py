from Game import *

# CLASSES #
game = Game()

def setup():
    size(400, 800)  

def draw():
    game.map.draw()
    print(game.map)