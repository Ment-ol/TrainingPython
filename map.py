from pygame import *
import math
game_map = [
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', "_", "_", "_", "A", "_", "_", "_", "_", "_", "A"],
    ['A', "_", "_", "_", "A", "_", "_", "_", "_", "_", "A"],
    ['A', "_", "A", "_", "A", "A", "A", "A", "A", "_", "A"],
    ['A', "_", "A", "_", "A", "_", "_", "A", "_", "_", "A"],
    ['A', "_", "A", "A", "A", "A", "_", "A", "_", "A", "A"],
    ['A', "_", "A", "_", "_", "_", "_", "A", "_", "A", "A"],
    ['A', "_", "A", "_", "_", "A", "_", "A", "_", "_", "A"],
    ['A', "_", "_", "_", "_", "A", "_", "A", "_", "_", "A"],
    ['A', "_", "_", "A", "_", "A", "_", "_", "_", "_", "A"],
    ['A', "_", "_", "A", "_", "A", "A", "_", "A", "-", "A"],
    ['A', "_", "A", "A", "_", "A", "_", "_", "A", "_", "A"],
    ['A', "_", "_", "_", "_", "_", "_", "_", "A", "A", "A"],
    ['A', "_", "_", "_", "_", "A", "_", "_", "_", "A", "A"],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
]
 #розмір квадратика вікна


class Block:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.rect = Rect(x, y, width, height)


    def draw(self, window):
        draw.rect(window, self.color, self.rect )

def make_map():
    SIZE = 800 / 15
    result = []
    y = 0
    for i in range(len(game_map)):
        ryadok = game_map[i]
        x = 0
        for block in ryadok:
            if block == 'A':
                new_block = Block((0, 255, 0), math.ceil(x), y,  SIZE, SIZE)
                result.append(new_block)
            x += SIZE
        y += SIZE
    return result