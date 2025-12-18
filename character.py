import pygame
import package

class Character:
    def __init__(self, position, amount_of_packages):
        self.set_total_packages(amount_of_packages)
        self.package_list = []
        self.x = position[0]
        self.y = position[1]
        self.packages_left = amount_of_packages
        sprite_sheet = pygame.image.load("Assets/Character/14x23 Idle christmas.png").convert_alpha()
        self.box_place_sound = pygame.mixer.Sound('Assets/sound/open-package-box-parcel-100334.mp3')
        self.error_sound = pygame.mixer.Sound('Assets/sound/error-mistake-sound-effect-incorrect-answer-437420.mp3')
        
        self.frames = [] 
        for i in range(4):
            frame = sprite_sheet.subsurface(pygame.Rect(i * 14, 0, 14, 23))
            frame = pygame.transform.scale_by(frame, 2.333333333)
            self.frames.append(frame)

        run_sheet = pygame.image.load("Assets/Character/14x24 Walk christmas.png").convert_alpha()
        self.run_frames = []
        for i in range(4):
            frame = run_sheet.subsurface(pygame.Rect(i * 14, 0, 14, 24)) 
            frame = pygame.transform.scale_by(frame, 2.333333333)
            self.run_frames.append(frame)

        jump_sheet = pygame.image.load("Assets/Character/16x25 Jump christmas.png").convert_alpha()
        self.jump_frames = []
        for i in range(5):
            frame = jump_sheet.subsurface(pygame.Rect(i * 16, 0, 16, 25))
            frame = pygame.transform.scale_by(frame, 2.333333333)
            self.jump_frames.append(frame)

        self.current_frame = 0
        self.timer = 0
        
        self.idle_pose = self.frames[0]
        
        self.total_packages_left=self.total_packages

        self.speed_y = 0
        self.facing_right = True
        self.is_moving = False

    def update_animation(self, dt):
        old_height = self.idle_pose.get_height()

        self.timer += dt
        if self.timer > 150:
            self.timer = 0
            self.current_frame += 1                
            if self.current_frame >= 5:
                self.current_frame = 0

        if not self.on_ground:
            animation_list = self.jump_frames
        elif self.is_moving:
            animation_list = self.run_frames
        else:
            animation_list = self.frames

        if self.current_frame >= len(animation_list):
            self.current_frame = 0
            
        image = animation_list[self.current_frame]
            
        if not self.facing_right:
            image = pygame.transform.flip(image, True, False)
                
        self.idle_pose = image

        new_height = self.idle_pose.get_height()
        
        if old_height != new_height:
            self.y += (old_height - new_height)
        
        self.is_moving = False 



    def set_height(self, position_y_platform):
        self.y = position_y_platform

    def playerfalling(self, dt):
        if not self.on_ground:
            gravity = 0.001
            self.speed_y += gravity * dt
            increase = self.speed_y * dt
            self.y  += increase

    def move_left(self):
        self.x -= 5
        self.facing_right = False
        self.is_moving = True

    def move_right(self):
        self.x += 5
        self.facing_right = True
        self.is_moving = True
        
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
        
    def amount_left(self):
        if self.total_packages_left > 0:
            self.total_packages_left-=1

    def get_total_packages(self):
        return self.total_packages_left
    
    def set_total_packages_left(self, amount):
        self.total_packages_left = amount
    
    def place_package(self, object_list):
        space_check_rect_right = pygame.rect.Rect(self.get_pos_x() + 30 , self.get_pos_y(), 50, 48)    
        space_check_rect_left = pygame.rect.Rect(self.get_pos_x() - 50 , self.get_pos_y(), 50, 48)
        placeable_left = True
        placeable_right = True  
        placed_packages = len(self.package_list)

        for objects in object_list: 
            if space_check_rect_right.colliderect(objects):
                placeable_right = False
            if space_check_rect_left.colliderect(objects):
                placeable_left= False
        
        
        if placeable_right and self.facing_right:
            if self.total_packages_left > 0:
                self.box_place_sound.play()
                self.package_list.append(package.Package([self.get_pos_x() + 30, self.get_pos_y()]))
                self.amount_left()
            else:
                self.error_sound.play()
        if not placeable_right and self.facing_right:
            self.error_sound.play()
        
        if placeable_left and not self.facing_right:
            if self.total_packages_left > 0:
                self.box_place_sound.play()
                self.package_list.append(package.Package([self.get_pos_x() - 50, self.get_pos_y()]))
                self.amount_left()
            else:
                 self.error_sound.play()
        if not placeable_left and not self.facing_right:
            self.error_sound.play() 