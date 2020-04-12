import pyxel

menu_box = 70, 40, 100, 120, 13


class App:
    def __init__(self):
        pyxel.init(240, 200, fps=30)

        self.menu = 0
        self.player_x = 60
        self.player_y = 60

        pyxel.run(self.update, self.draw)

    #   UPDATE FUNCTION
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.movement()

    #   DRAW FUNCTION
    def draw(self):
        pyxel.cls(0)

        pyxel.mouse(visible=False)

        pyxel.circ(self.player_x, self.player_y, 1, 3)

        self.menu_load()
        self.coords()

    #   THE MENU
    def menu_load(self):
        if pyxel.btnr(pyxel.KEY_M):
            self.menu += 1
        if self.menu == 1:
            pyxel.rectb(*menu_box)
            pyxel.text(menu_box[0] + 2, menu_box[1] + 2, "THE MENU", 1)
            pyxel.mouse(visible=True)
        else:
            self.menu = 0

    #   COORDS TOOL
    def coords(self):
        pyxel.rect(0, 0, 40, 18, 0)
        pyxel.text(1, 1, "X: " + str(self.player_x), 10)
        pyxel.text(1, 11, "Y: " + str(self.player_y), 10)

    def movement(self):
        if pyxel.btn(pyxel.KEY_A):
            self.player_x -= 1
        if pyxel.btn(pyxel.KEY_D):
            self.player_x += 1
        if pyxel.btn(pyxel.KEY_W):
            self.player_y -= 1
        if pyxel.btn(pyxel.KEY_S):
            self.player_y += 1


App()
