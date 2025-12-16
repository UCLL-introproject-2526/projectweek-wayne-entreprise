import pygame

from random import randint

class Package:
    def __init__(self):
        self.x = 0
        self.y = -100
        set_color()

    
    def set_color(self):
        rand = randint(1,3)
        if rand == 1:
            self.color = (230,33,33) #red
        elif rand == 2:
            self.color = (33,230,33) #green
        else:
            self.color = (33,33,230) #blue
    
    def check_for_collission(self, place_coördinates):
        ...
    
    def place():
        ...

p = Package()