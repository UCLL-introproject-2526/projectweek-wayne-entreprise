import pygame

class Character:
    def __init__(self, position, amount_of_packages):
        self.__packages = []
        self.x = position[0]
        self.y = position[1]
        self.idle_pose = pygame.image.load("Assets/Character/14x23 Idle christmas.png").convert_alpha()
        self.idle_pose = self.idle_pose.subsurface(pygame.Rect(0,0,14,23))
        #self.idle_pose = pygame.transform.scale_by(self.idle_pose, 1)
        
        #haal alle afbeeldingen uit idle_pose en steek ze in een lijst
        self.sheet_width = self.spritesheet.get_width()
        self.frame_width = self.sheet_width // 8  
        self.frame_height = self.spritesheet.get_height()
        self.frames_front = []
        self.frames_side = []
        
        for i in range(8):
            # Maak een 'uitsnede' (subsurface) voor elk frame
            frame = self.spritesheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            
            if i < 4:
                self.frames_front.append(frame) # Eerste 4 zijn voorkant
            else:
                self.frames_side.append(frame)  # Laatste 4 zijn zijkant
        #einde lijst steken


    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
        
    def move_up(self):
        self.y -= 5
        
    def move_down(self):
        self.y += 5

    def place_package(self):
        ...
