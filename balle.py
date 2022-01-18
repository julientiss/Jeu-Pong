import random

from pygame.math import Vector2

import core



class Balle:
    def __init__(self,w=1200,h=800):
        self.pos = Vector2(400,100)
        self.vel = Vector2(2,5)
        self.acc = Vector2()
        self.r = 10
        self.color=(0,0,225)

    def applyForce(self,force):
        pass

    def intersection(self, objet):
        DeltaX = self.pos.x - max(objet.pos.x, min(self.pos.x, objet.pos.x + objet.longeur));
        DeltaY = self.pos.y - max(objet.pos.y, min(self.pos.y, objet.pos.y + objet.hauteur));
        return (DeltaX * DeltaX + DeltaY * DeltaY) < (self.r * self.r);

    def update(self,raquette):
        self.pos+=self.vel

        if self.intersection(raquette):
            self.vel.y *= -1


    def edge(self,sizes):
        if self.pos.x <=0:
            self.vel.x *= -1
            self.pos.x = 10
        if self.pos.x >= sizes[0]:
            self.vel.x *= -1
            self.pos.x = sizes[0] - 10
        if self.pos.y <= 0:
            self.vel.y *= -1
            self.pos.y = 10
        if self.pos.y >= sizes[1]:
            return True
        return False

    def show(self):
        core.Draw.circle(self.color,self.pos,self.r)