import pyxel
import time


class App:
    def __init__(self):
        pyxel.init(240, 200, fps=30)
        # 30 FPS = 1 / 30 = 0.03s per individual frame

        self.player_x = 60
        self.player_y = 60
        self.dt = 0.03
        self.gravity = 5  # Random value for Gravity
        self.vel = 0
        self.speed = 0
        self.t = None
        self.dist = 0
        self.new_dist = None

        pyxel.run(self.update, self.draw)

    #   UPDATE FUNCTION
    def update(self):
        self.movement()

    #   DRAW FUNCTION
    def draw(self):
        pyxel.cls(0)

        #   The player object
        pyxel.circ(self.player_x, self.player_y, 1, 10)

        self.coords()

    #   MOVEMENT FUNCTIONs
    def movement(self):
        if pyxel.btn(pyxel.KEY_S):
            self.player_y = self.player_y + (self.dt * self.vel)
            self.vel = self.vel + (self.dt * self.gravity)
            self.t = time.perf_counter()
            self.dist = self.player_y - 60
            self.speed = round(self.dist / self.t, 2)
            print(self.t)
        if pyxel.btnr(pyxel.KEY_S):
            self.new_dist = self.player_y
            self.dist -= self.player_y
            self.speed = 0
            self.t = time.perf_counter()
            print(self.t)
            print(self.dist)
            self.vel = 0

    #   COORDS TOOL
    def coords(self):
        pyxel.rect(0, 0, 40, 18, 0)
        pyxel.text(1, 1, "Speed: " + str(self.speed) + " px/s", 10)
        pyxel.text(1, 11, "Y: " + str(self.player_y), 10)
        pyxel.line(0, 60, 240, 60, 9)
        pyxel.line(0, 160, 240, 160, 9)


App()
