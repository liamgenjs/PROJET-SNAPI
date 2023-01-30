from Game import *

# CLASSES #
game = Game()

def setup():
    size(800, 400)  

def draw():
    game.map.draw()