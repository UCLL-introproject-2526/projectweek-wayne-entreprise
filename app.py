import pygame
import character
import package
import goal
import Platform


def main():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
    start_image = pygame.image.load('Assets/affiche.webp')
    start_image = pygame.transform.scale_by(start_image, 0.5357142857)
    start = True
    running = True
    while start and running:
        screen.blit(start_image, (0,154))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    running = False
                if event.key == pygame.K_1:
                    game_loop(1) 
                    start = False
                 
        klok.tick(60)
        pygame.display.flip()
    running = True
    
    if start: 
        running = game_loop(1)
        game_loop(2)
        game_loop(3)
        game_loop(4)
        game_loop(5)
        game_loop(6)
        game_loop(7)

def game_loop(level):
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst")
    
    # stop music 
    #pygame.mixer.music.stop() 
    screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
    running = True
    loop2 = True
    loop3 = True

    start_image = pygame.image.load('Assets/affiche.webp')
    start_image = pygame.transform.scale_by(start_image, 0.5357142857)

    if level == 1:
        start_coordinates = start_x, start_y = (20, 400)
        packages = 10
        platforms = [
        Platform.Platform(200, 450, 64, 32),
        Platform.Platform(270, 450, 64, 32)
        ]
    if level == 2:
        start_coordinates = start_x, start_y = (20, 400)
        packages = 40
        platforms = [
        Platform.Platform(150, 500, 64, 32),
        Platform.Platform(220, 500, 64, 32),
        Platform.Platform(400, 400, 64, 32),
        Platform.Platform(470, 400, 64, 32),
        Platform.Platform(540, 400, 64, 32)
        ]


    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.351568)

    c1 = character.Character(start_coordinates, packages)
    c1.on_ground = False
    
    g1 = goal.Goal(screen)
    move_left = False
    move_right = False

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
                    c1.set_direction(False)
                    c1.set_direction(False)
                if event.key == pygame.K_RIGHT:
                    move_right = True
                    c1.set_direction(True)
                    c1.set_direction(True)
                if event.key == pygame.K_SPACE:
                    c1.place_package(all_objects)
                if event.key == pygame.K_UP:
                    c1.jump()
                if event.key == pygame.K_r:
                    c1.x = start_x
                    c1.y = start_y
                    c1.clean_packages()
                if event.key == pygame.K_f:
                    music.set_volume(0)
                if event.key == pygame.K_g:
                    music.set_volume(0.1)
                

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
        if not c1.on_ground:
            c1.on_ground = False
        c1_hitbox = pygame.Rect(c1.x+6, c1.y + c1.idle_pose.get_height()-3 , 18, 8)


        screen.blit(background, (0,0))

        win_rectangle = pygame.rect.Rect(600, 160, 32, 32)
        pygame.draw.rect(screen, (0, 255, 0), win_rectangle)

        floor_y = screen.get_height() * 3//4 - 30
        if c1_hitbox.colliderect(win_rectangle):
            loop2 = g1.win()
        
        char_height = c1.idle_pose.get_height()
            
        for p in platforms:
            if c1_hitbox.colliderect(p.rect):
                if c1.speed_y > 0 and c1_hitbox.bottom < p.rect.bottom:
                    c1.y = p.rect.top - char_height 
                    c1.speed_y = 0                  
                    c1.on_ground = True

        # Package collision detection
        for pkg in c1.package_list:
            screen.blit(pkg.image, (pkg.x, pkg.y))
            if not pkg.freeze:
                pkg.package_falling(dt)
        
        package_platforms = []

        for pkg1 in c1.package_list:
            pkg_rect_lower_own = pkg1.get_rect_lower()
            pkg_rect_upper_own = pkg1.get_rect_upper()

            for pkg2 in c1.package_list:
                if pkg1 is pkg2:
                    continue 
                pkg_rect_upper = pkg2.get_rect_upper()
                if pkg_rect_lower_own.colliderect(pkg_rect_upper):
                    pkg1.y = pkg_rect_upper.top - 48
                    pkg1.freeze = True
            if pkg1.freeze:
                package_platforms.append(pkg_rect_upper_own)
        
        
        all_objects = [*package_platforms,*platforms]
        
        for platform in package_platforms:
            if c1_hitbox.colliderect(platform):
                if c1.speed_y > 0 and c1_hitbox.bottom <= platform.bottom + 5:
                    c1.y = platform.top - char_height +1
                    c1.speed_y = 0
                    c1.on_ground = True
                    # print("touching")
        
        touching_object = None
        for obj in all_objects:
            if c1_hitbox.colliderect(obj):
                touching_object = True
        if not touching_object:
            c1.on_ground = False

        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True
        for p in platforms:
            screen.blit(p.image, p.rect)

        c1.update_animation(dt)
        screen.blit(c1.idle_pose, (c1.x, c1.y))
        #print(c1.y)
        # print(package_platforms)
        pygame.display.flip()
        

        print(f"{c1.y} {c1.x} ,  {c1.package_list}")
        # print(c1.on_ground)

    while running and loop3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        klok.tick(60)
    pygame.quit()

pygame.init()
music = pygame.mixer.Sound('Assets/sound/Chill Pulse - Jingle Bell Rock (freetouse.com).mp3') 
music.play(-1)
music.set_volume(0.1)
main()
