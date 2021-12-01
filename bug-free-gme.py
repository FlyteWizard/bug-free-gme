# Imports
import pyxel
import random

# Global Scenes
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_OVER = 2

# Application
class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Bug Free Gme")
        pyxel.mouse(True)

        pyxel.load("assets/bug-free-gme.pyxres")

        self.scene = SCENE_TITLE

        self.player_x = 60
        self.player_y = 60
        self.player_orientation = 16
        self.music_icon = 16
        self.music_playing = False
        self.bug = False

        pyxel.run(self.update, self.draw)

    def toggle_music(self):
        """Toggle music on/off
        """

        # Toggle
        if self.music_playing:
            self.music_icon = 16
            pyxel.stop(0)
            self.music_playing = False
        else:
            self.music_icon = 0
            pyxel.playm(0, loop=True)
            self.music_playing = True

    def update(self):
        """Update the game state.
        """

        # Music Toggle
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            if (pyxel.mouse_x > 0 and pyxel.mouse_x < 16 and pyxel.mouse_y > 0 and pyxel.mouse_y < 16):
                self.toggle_music()
        if (pyxel.btnp(pyxel.KEY_M)):
            self.toggle_music()

        # Quit Game
        if pyxel.btnp(pyxel.KEY_ENTER):
            pyxel.quit()

        # Scene Update
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
            if pyxel.btnp(pyxel.KEY_Q):
                self.scene = SCENE_PLAY
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                if (pyxel.mouse_x >= 50 and pyxel.mouse_x <= 108 and pyxel.mouse_y >= 55 and pyxel.mouse_y <= 59):
                    self.scene = SCENE_PLAY
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                if (pyxel.mouse_x >= 50 and pyxel.mouse_x <= 128 and pyxel.mouse_y >= 65 and pyxel.mouse_y <= 69):
                    pyxel.quit()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene(bug=False)
            if pyxel.btnp(pyxel.KEY_X):
                self.scene = SCENE_OVER
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                if (pyxel.mouse_x >= 55 and pyxel.mouse_x <= 105 and pyxel.mouse_y >= 40 and pyxel.mouse_y <= 44):
                    self.scene = SCENE_OVER
            if (pyxel.btnp(pyxel.KEY_H)):
                self.update_play_scene(bug=True)
            if (pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)):
                if (pyxel.mouse_x < self.player_x + 16 and
                    pyxel.mouse_x > self.player_x and
                    pyxel.mouse_y < self.player_y + 16 and
                    pyxel.mouse_y > self.player_y):
                    self.update_play_scene(bug=True)
        elif self.scene == SCENE_OVER:
            self.update_over_scene()

    def update_title_scene(self):
        """Update the title scene.
        """

        pass

    def update_over_scene(self):
        """Update the over scene.
        """

        pass

    def update_play_scene(self, bug):
        """Update the play scene.
        """

        # Set Bug
        if bug:
            self.bug = True

        # Update Player
        self.update_player()

    def update_player(self):
        """Update the player.
        """

        # Move Player
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            self.player_orientation = 16

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = max(self.player_x - 2, 0)
            self.player_orientation = 0

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.player_y = max(self.player_y - 2, 0)
            self.player_orientation = 32

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)
            self.player_orientation = 48

    def draw(self):
        """Draw the game.
        """

        # Background
        pyxel.cls(7)

        # Music Icon
        pyxel.blt(0, 0, 0, self.music_icon, 16, 16, 16)

        # Bug
        if self.bug:
            pyxel.text(self.player_x + 16, self.player_y + 1, "!", 3)
            pyxel.text(pyxel.mouse_x + 8, pyxel.mouse_y, "Ouch!", 9)
            pyxel.text(random.randint(0, 160), random.randint(0, 120), "!", random.randint(0, 15))
            pyxel.text(80, 100, "You Hit Me :'(", 2)

        # Draw Scene
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        if self.scene == SCENE_PLAY:
            self.draw_play_scene()
        if self.scene == SCENE_OVER:
            self.draw_over_scene()

    def draw_title_scene(self):
        """Draw the title scene.
        """

        # Title
        pyxel.text(55, 40, "Bug Free Game", 1)

        # Instructions
        pyxel.text(50, 55, "Press Q to quit", 9)
        pyxel.text(50, 65, "Press Enter to start", 4)

    def draw_play_scene(self):
        """Draw the play scene.
        """

        # Glitch Title
        pyxel.text(55, 40, "Bug Free Game", pyxel.frame_count % 16)

        # Player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            self.player_orientation,
            0,
            16,
            16,
        )

    def draw_over_scene(self):
        """Draw the over scene.
        """

        # Title
        pyxel.text(55, 40, "wElp - Gme OvEr", 10)

App()
