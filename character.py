import pygame

class Character:
    def __init__(self, position, amount_of_packages):
        self.total_packages = amount_of_packages
        self.__packages = []
        self.x = position[0]
        self.y = position[1]
        self.idle_pose = pygame.image.load("Assets/Character/14x23 Idle christmas.png").convert_alpha()
        self.idle_pose = self.idle_pose.subsurface(pygame.Rect(0,0,14,23))
        self.speed_y = 0
        self.idle_pose = pygame.transform.scale_by(self.idle_pose, 2.333333333)
        self.facing_left = True

    def set_height(self, position_y_platform):
        self.y = position_y_platform

    def playerfalling(self, dt):
        gravity = 0.0005
        self.speed_y += gravity * dt
        increase = self.speed_y * dt
        self.y  += increase

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
        
    def jump(self):
        if self.on_ground:
            self.speed_y = -0.35
            self.on_ground = False

    def get_pos_x(self):
        return self.x
    
    def get_pos_y(self):
        return self.y
    
    def set_direction(self, boolean):
        self.facing_left = boolean
            
    def place_package(self):
        placed_packages = 0
        if placed_packages < self.total_packages:
            if self.facing_right:
                packages.append(Package((self.get_pos_x() + 11, self.get_pos_y)))
            else:
                packages.append(Package((self. get_pos_x() - 11, self.get_pos_y)))
        