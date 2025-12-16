import pygame
def main():
    ...


def create_main_surface():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst")

    screen_size = (1024, 768)
    screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    running = True
    position = 0
    move_x = 0
    move_y=0
    while running:
        pygame.draw.circle(screen, (255,100,255), (position,200), 20)
        pygame.display.flip()
        screen.fill((0,0,0))
        klok.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    move_x = -2
                if event.key == pygame.K_RIGHT:
                    move_x = 2
                if event.key == pygame.K_SPACE:
                    move_y +=2
        position += move_x
        if position < 0:
            position = 0
        if position > 1024:
            position = 1024
    pygame.quit()


create_main_surface()

