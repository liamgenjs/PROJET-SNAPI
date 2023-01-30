from Tuiles import Tuiles
class Map:

    def __init__(self):
        self.tuiles = Tuiles().tuiles
        self.tab_img_tuiles = []

    def set(self):
        for i in range (1, 20):
            self.tab_img_tuiles.append(loadImage("Cases/" + str(i) + ".png"))

    def draw(self):
        self.set()
        print("ok")
        for x in range (0,20):
            for y in range(0,15):
                num_tuile = self.tuiles[y][x]
                image(self.tab_img_tuiles[num_tuile - 1], 50+16*x, 16*y)