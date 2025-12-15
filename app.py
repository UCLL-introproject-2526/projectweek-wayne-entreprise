import pygame


def main():
    ...


def create_main_surface():
    pygame.init()
    klok = pygame.time.Clock()
    #hey niels hoe gaat het?
    screen_size = (1024, 768)

    screen=pygame.display.set_mode(screen_size)
    pygame.draw.circle(screen, (255,100,255), (10,10), 100)
    pygame.display.flip()
    
while True:
    create_main_surface()

