import pygame
import character
import package
import goal


def main():
    ...

def game_loop():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    running = True

    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.15625)
    screen = pygame.display.set_mode((320,320), pygame.FULLSCREEN | pygame.SCALED)

    c1 = character.Character((0, 160), 10)
    
    g1 = goal.Goal(screen)
    move_left = False
    move_right = False
    while running:
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
        dt = klok.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False

        if move_left:
            c1.move_left()
        elif move_right:
            c1.move_right()
        else:
            ...

        screen.blit(background, (0,0))
        screen.blit(c1.idle_pose, (c1.x, c1.y))
        rectangle = pygame.rect.Rect(150, 160, 32, 32)
        pygame.draw.rect(screen, (255, 0, 0), rectangle)
        if c1_hitbox.colliderect(rectangle):
            running = g1.win()

    
        c1.playerfalling(dt)
        
        pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        klok.tick(60)
    pygame.quit()

game_loop()
