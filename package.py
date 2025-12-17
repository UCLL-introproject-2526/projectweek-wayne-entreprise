import pygame

from random import randint

class Package:
    def __init__(self, position, screen_height=720):
        self.x = position[0]
        self.y = position[1]
        self.screen_height = screen_height
        self.floor_y = screen_height * 3 // 4 - 30
        self.set_image()
        self.speed_y = 0
        self.stopped = False

    def __repr__(self):
        return f"Package(x={self.x}, y={self.y})"
    
    def set_image(self):
        rand = randint(1,3)
        
        if rand == 1:
            self.image = pygame.image.load("Assets/Presents/present_blue_25x24.png").convert_alpha()
            
        elif rand == 2:
            self.image = pygame.image.load("Assets/Presents/present_green_25x24.png").convert_alpha()
        else:
            self.image = pygame.image.load("Assets/Presents/present_yellow25x24.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,48))
    
    def check_for_collission(self, place_coördinates):
        ...
    
    def get_rect(self):
        """Return the collision rectangle for this package"""
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    
    def package_falling(self, dt):
        gravity = 0.001
        self.speed_y += gravity * dt
        increase = self.speed_y * dt
        self.y += increase
        # Stop packages at floor level (above 1/4 of screen)
        if self.y >= self.floor_y - 48 or self.stopped:
            self.y = self.floor_y - 48
            self.stopped = True
            self.speed_y = 0

