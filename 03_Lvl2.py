import pygame
import character
import package
import goal
import Chimney
import Platform

def game_tuto():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    running = True
    startscreen=True
    start=pygame.image.load('Assets/affiche.webp')
    start = pygame.transform.scale_by(start, 0.5357142857)
    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.351568)
    screen = pygame.display.set_mode((720,720), pygame.FULLSCREEN | pygame.SCALED)
    c1 = character.Character((0, 400), 6)
    c1.on_ground=False
    g1 = goal.Goal(screen)
    move_left = False
    move_right = False
    font_expl=pygame.font.Font(None,size=25)
    text_explain=font_expl.render(f'Are you ready for lvl2?',True,(255,255,255))
    text_lvl=font_expl.render(f'LVL2',True,(255,255,255))
    packages_left=font_expl.render(f'Total amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
    flag=pygame.image.load('Assets/flag/Flag_18x32.png')
    flag=pygame.transform.scale_by(flag,1.5)

    while startscreen:
        screen.blit(start, (0,154))
        screen.blit(text_explain,(15,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    startscreen = False
                if event.key == pygame.K_SPACE:
                    startscreen = False
        klok.tick(60)
        pygame.display.flip()

    chimneys=[Chimney.Chimney(200,screen.get_height()*3/4-180,100,150),
                Chimney.Chimney(400,screen.get_height()*3/4-180,100,150),
              Chimney.Chimney(610,screen.get_height()*3/4-180,100,150)]
    platforms = [
    Platform.Platform(350, 100, 64, 32),
    Platform.Platform(450, 200, 64, 32),
    Platform.Platform(600, 250, 64, 32)
    ]
    all_objects = [*chimneys,*platforms]
    while running:
        dt = klok.tick(60)  
        screen.blit(background,(0,0))
        screen.blit(text_lvl,(100,20))
        screen.blit(packages_left,(300,20))
        c1.update_animation(dt)
        screen.blit(c1.idle_pose, (c1.x, c1.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    if c1.x>0:
                        move_left = True
                if event.key == pygame.K_RIGHT:
                    if c1.x<screen.get_width():
                        move_right = True
                if event.key == pygame.K_UP:
                    c1.jump()
                    
                if event.key == pygame.K_SPACE:
                    c1.place_package()
                    packages_left=font_expl.render(f'Total amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                    if c1_hitbox.colliderect(flag_hitbox):
                        text_explain=font_expl.render('',True,(255,255,255))
                        text_explain2=font_expl.render('',True,(255,255,255))
                        screen.blit(text_explain,(20,50))
                        screen.blit(text_explain2,(20,80))
                        running = g1.win()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False

        
        if move_left and c1.x>0:
            c1.move_left()
        elif move_right and c1.x<background.get_width():
            c1.move_right()
        else:
            ...
        char_height = c1.idle_pose.get_height()
        char_width = c1.idle_pose.get_width()
        c1.playerfalling(dt)
        if not c1.on_ground:
            c1.on_ground = False
        floor_y = screen.get_height() * 3/4-30
        #hitboxen
        flag_hitbox=pygame.Rect(630,400,flag.get_width(),flag.get_height())
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
        ##
        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True
        
        for object in all_objects:
            screen.blit(object.image, object.rect)  

        klok.tick(60)
        pygame.display.flip()


game_tuto()