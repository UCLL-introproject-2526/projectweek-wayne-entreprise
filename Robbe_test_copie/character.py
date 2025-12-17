import pygame

class Character:
    def __init__(self, position, amount_of_packages):
        self.x = position[0]
        self.y = position[1]
        self.idle_pose = pygame.image.load("../Assets/Character/14x23 Idle christmas.png").convert_alpha()
        self.idle_pose = self.idle_pose.subsurface(pygame.Rect(0,0,14,23))
        self.idle_pose = pygame.transform.scale_by(self.idle_pose, 2.333333333)
        
        self.speed_y = 0
        self.on_ground = False 

    def playerfalling(self, dt):
        gravity = 0.0005
        self.speed_y += gravity * dt
        self.y += self.speed_y * dt


    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
        
    def jump(self):
        if self.on_ground:
            self.speed_y = -0.35
            self.on_ground = False