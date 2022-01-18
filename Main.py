# jeu squash solo

import pygame
import core
from balle import Balle
from raquette import Raquette


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 600]
    core.memory("IA", False)
    core.memory("b", Balle())
    core.memory("GameOver", False)
    core.memory("Score", 0)
    core.memory('r', Raquette(800, 600))



    print("Setup END-----------")


def run():


    # Si pas perdu
    if not core.memory("GameOver"):
        core.cleanScreen()

        # raquette
        if core.getMouseLeftClick():
            core.memory('r').update(core.getMouseLeftClick())

        if core.memory("IA"):
            core.memory('r').pos.x = core.memory('b').pos.x - core.memory('r').longeur / 2

        # balle
        core.memory('b').update(core.memory('r'))

        if core.memory('b').edge(core.WINDOW_SIZE):
            core.memory("GameOver", True)

        # Affichage
        core.memory('b').show()
        core.memory('r').show()

    else:  # si Perdu
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render("Game Over", False, (255, 0, 0))
        core.screen.blit(textsurface, (core.WINDOW_SIZE[0] / 2 - 250, core.WINDOW_SIZE[1] / 2 - 50))








core.main(setup, run)