import pyxel

#   SPRITES
skier = 0, 36, 44, 7, 11, 2
skier_right = 0, 3, 44, 9, 11, 2
skier_left = 0, 3, 44, -9, 11, 2
skier_stop = 0, 19, 44, 9, 11, 2
tree = 0, 8, 56, 7, 8, 2
pole = 0, 3, 58, 3, 6, 2


# --------------------------------------------- #

class App:
    def __init__(self):
        pyxel.init(240, 200, fps=30)

        pyxel.load("assets.pyxres", image=True)

        self.player_x = 60
        self.player_y = 30
        self.speed = 0.5

        self.trail_x = []
        self.trail_y = []

        pyxel.run(self.update, self.draw)

    # ------------------------------------------------------------ #
    #   UPDATE FUNCTION
    def update(self):
        self.movement()
        self.slalom()

    #   THE SLALOM FUNCTION
    def slalom(self):
        self.player_y += self.speed

        if self.player_y > pyxel.height:
            self.player_y = 1

    #   PLAYER MOVEMENT FUNCTION
    def movement(self):
        if pyxel.btn(pyxel.KEY_A):
            self.player_x -= self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.player_x += self.speed

        if pyxel.btn(pyxel.KEY_SPACE) and self.speed >= 0:
            self.speed -= 0.5
        else:
            self.speed = 0.5

    # ------------------------------------------------------------ #
    #   SPRITE CHANGE FUNCTION
    def skier(self):
        pyxel.blt(self.player_x, self.player_y, *skier)

        if pyxel.btn(pyxel.KEY_A):
            pyxel.blt(self.player_x, self.player_y, *skier_left)
        elif pyxel.btn(pyxel.KEY_D):
            pyxel.blt(self.player_x, self.player_y, *skier_right)
        elif pyxel.btn(pyxel.KEY_SPACE):
            pyxel.blt(self.player_x, self.player_y, *skier_stop)

    #   SKI TRAIL FUNCTION
    def trail(self):
        self.trail_x.append(self.player_x)
        self.trail_y.append(self.player_y)
        # print(self.trail_x)
        # print(self.trail_y)
        trail_x = self.trail_x[len(self.trail_x) - 30:len(self.trail_x)]
        trail_y = self.trail_y[len(self.trail_y) - 30:len(self.trail_y)]
        # print(trail_x)
        # print(len(trail_x))
        if self.player_y < pyxel.height - 5 and self.player_x < pyxel.width - 5:
            if len(trail_x) and len(trail_y) < 10:
                pass
            elif len(trail_x) and len(trail_y) >= 30:
                pyxel.line(trail_x[0], trail_y[0], trail_x[28], trail_y[28], 13)
                pyxel.line(trail_x[0] - 3, trail_y[0] + 3, trail_x[28] - 3, trail_y[28] + 3, 13)
        else:
            self.trail_y.clear()
            self.trail_x.clear()

    #   DRAW FUNCTION
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 240, 200, 7)
        pyxel.mouse(visible=False)

        self.skier()
        self.trail()


App()
