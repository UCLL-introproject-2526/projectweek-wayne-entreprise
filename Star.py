import pygame
import random

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        star_sheet = pygame.image.load("Assets/Star/Star_3x3.png").convert_alpha()
        

        self.frames = [] 
        for i in range(2):
            frame = star_sheet.subsurface(pygame.Rect(i * 3, 0, 3, 3))
            frame = pygame.transform.scale_by(frame, (3, 3))
            self.frames.append(frame)

        self.current_frame = 0
        self.current_frame = random.randint(0, len(self.frames) - 1)
        self.timer = random.randint(0, 300) 
        self.image = self.frames[self.current_frame]

    def update(self, dt):
        self.timer += dt
        if self.timer > 300: 
            self.timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))