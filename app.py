import pygame
import character
import package
import goal
import Platform


def main():
    ...

def game_loop():
    packages = []
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
    running = True
    loop1 = True
    loop2 = True
    loop3 = True

    start_image = pygame.image.load('Assets/affiche.webp')
    start_image = pygame.transform.scale_by(start_image, 0.5357142857)

    p1 = Platform.Platform(200, 450, 64, 32)

    while running and loop1:
        screen.blit(start_image, (0,154))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    loop1 = False
        klok.tick(60)
        pygame.display.flip()

    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.351568)
    
    
    c1 = character.Character((0, 160), 10)
    
    g1 = goal.Goal(screen)
    move_left = False
    move_right = False

    facing_right = True

    ##TEMP
    total_packages = 30

    while running and loop2:
        dt = klok.tick(60)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    move_left = True
                    facing_right = False
                if event.key == pygame.K_RIGHT:
                    move_right = True
                    facing_right = True
                if event.key == pygame.K_SPACE:
                    c1.place_package()
                if event.key == pygame.K_UP:
                    c1.jump()
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False

        if move_left:
            c1.move_left()
        if move_right:
            c1.move_right()
        else:
            ...

        c1.playerfalling(dt)
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())

        screen.blit(background, (0,0))

        win_rectangle = pygame.rect.Rect(150, 160, 32, 32)
        screen.blit(g1.image, (250, 50))


        hitbox_floor=pygame.Rect(0,screen.get_height()*3/4,screen.get_width(),screen.get_height()*1/4)
        print(hitbox_floor.top)

        if c1_hitbox.colliderect(win_rectangle):
            loop2 = g1.win()
        
        char_height = c1.idle_pose.get_height()
        char_width = c1.idle_pose.get_width()

        if c1_hitbox.colliderect(p1.rect):
            if c1.speed_y > 0 and c1_hitbox.bottom < p1.rect.bottom:
                c1.y = p1.rect.top - char_height 
                c1.speed_y = 0                   
                c1.on_ground = True            

        floor_y = screen.get_height() * 3/4 

        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True           
        
        screen.blit(p1.image, p1.rect)

        screen.blit(c1.idle_pose, (c1.x, c1.y))
        #print(c1.y)


        pygame.display.flip()

    while running and loop3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        klok.tick(60)
    pygame.quit()

game_loop()
