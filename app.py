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
    background = pygame.transform.scale_by(background, 0.351568)
    screen = pygame.display.set_mode((720,720), pygame.FULLSCREEN | pygame.SCALED)
    
    c1 = character.Character((0, 160), 10)
    
    g1 = goal.Goal(screen)
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    while running:
        dt = klok.tick(60)  
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
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
                if event.key == pygame.K_SPACE:
                    c1.y = 0
                if event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_UP:
                    move_up = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_DOWN:
                    move_down = False
                if event.key == pygame.K_UP:
                    move_up = False

        if move_left:
            c1.move_left()
        elif move_right:
            c1.move_right()
        elif move_up:
            c1.move_up()
        elif move_down:
            c1.move_down()
        else:
            ...

        screen.blit(background, (0,0))
        screen.blit(c1.idle_pose, (c1.x, c1.y))
        win_rectangle = pygame.rect.Rect(150, 160, 32, 32)
        pygame.draw.rect(screen, (255, 0, 0), win_rectangle)
        hitbox_floor=pygame.Rect(0,screen.get_height()*3/4,screen.get_width(),screen.get_height()*(1/4)+24)

        if c1_hitbox.colliderect(win_rectangle):
            running = g1.win()
        if c1_hitbox.colliderect(hitbox_floor):
            c1.speed_y=0
            
               
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
