import pygame
import package

class Character:
    def __init__(self, position, amount_of_packages):
        self.set_total_packages(amount_of_packages)
        self.package_list = []
        self.x = position[0]
        self.y = position[1]

        sprite_sheet = pygame.image.load("Assets/Character/14x23 Idle christmas.png").convert_alpha()
        
        self.frames = [] 
        for i in range(4):
            frame = sprite_sheet.subsurface(pygame.Rect(i * 14, 0, 14, 23))
            frame = pygame.transform.scale_by(frame, 2.333333333)
            self.frames.append(frame)

        self.current_frame = 0
        self.timer = 0
        
        self.idle_pose = self.frames[0]
        


        self.speed_y = 0
        self.facing_right = True

    def update_animation(self, dt):
        self.timer += dt
        if self.timer > 150:
            self.timer = 0
            self.current_frame += 1                
            if self.current_frame >= 4:
                self.current_frame = 0
            
        image = self.frames[self.current_frame]
            
        if not self.facing_right:
            image = pygame.transform.flip(image, True, False)
                
        self.idle_pose = image



    def set_height(self, position_y_platform):
        self.y = position_y_platform

    def playerfalling(self, dt):
        gravity = 0.001
        self.speed_y += gravity * dt
        increase = self.speed_y * dt
        self.y  += increase

    def move_left(self):
        self.x -= 5
        self.facing_right = False

    def move_right(self):
        self.x += 5
        self.facing_right = True
        
    def jump(self):
        if self.on_ground:
            self.speed_y = -0.35
            self.on_ground = False

    def get_pos_x(self):
        return self.x
    
    def get_pos_y(self):
        return self.y
    
    def set_direction(self, boolean):
        self.facing_right = boolean

    def set_total_packages(self,amount):
        self.total_packages = amount
                
    def clean_packages(self):
        self.package_list = []
    
    def get_total_packages(self):
        return self.total_packages

    def place_package(self):
        placed_packages = len(self.package_list)
        if placed_packages < self.total_packages:
            if self.facing_right:
                self.package_list.append(package.Package([self.get_pos_x() + 30, self.get_pos_y()]))
            else:
                self.package_list.append(package.Package([self.get_pos_x() - 30, self.get_pos_y()]))
        print(len(self.package_list))
        print((self.package_list))
