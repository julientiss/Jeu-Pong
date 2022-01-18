import random

from pygame.math import Vector2

import core


class Raquette:
    def __init__(self,w=1200,h=800):
        self.pos = Vector2(random.randint(0,w), h-20)
        self.longeur=100
        self.hauteur=10
        self.color=(0,255,0)
        self.acc = Vector2()
        self.vel = Vector2()
        self.maxAcc = 100
        self.maxSpeed = 100



    def update(self,clique):

        vect = Vector2(clique[0], self.pos.y)
        self.acc = vect - self.pos

        if self.acc.length() > self.maxAcc:
            self.acc.scale_to_length(self.maxAcc)

        self.vel += self.acc
        if self.vel.length() > self.maxSpeed:
            self.vel.scale_to_length(self.maxSpeed)
        self.acc = Vector2(0, 0)

        self.pos += self.vel

        self.vel = Vector2(0, 0)


    def show(self):
        core.Draw.rect(self.color,(self.pos.x,self.pos.y,self.longeur,self.hauteur))