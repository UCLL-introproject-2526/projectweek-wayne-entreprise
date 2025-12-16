import pygame
import character
import goal

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

    while running:
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
                if event.key == pygame.K_SPACE:
                    c1.y = 0 # Debug reset
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

        c1.playerfalling(dt)
        
        
        char_height = c1.idle_pose.get_height()
        char_width = c1.idle_pose.get_width()
        c1_hitbox = pygame.Rect(c1.x, c1.y, char_width, char_height)

        win_rectangle = pygame.rect.Rect(150, 160, 32, 32)
        if c1_hitbox.colliderect(win_rectangle):
            running = g1.win()

        floor_y = screen.get_height() * 3/4  

        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True           
        else:
            c1.on_ground = False          

        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (255, 0, 0), win_rectangle)
        
        screen.blit(c1.idle_pose, (round(c1.x), round(c1.y)))

        pygame.display.flip()

    while running: 

         break
         
    pygame.quit()

game_loop()