import pygame
import character
import package
import goal
import Platform


def main():
    ...

def game_loop():
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

    platforms = [
    Platform.Platform(200, 450, 64, 32),
    Platform.Platform(270, 450, 64, 32)
    ]

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
    
    screen_height = screen.get_height()
    c1 = character.Character((0, 400), 40)
    
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
        c1.on_ground = False
        c1.playerfalling(dt)
        c1_hitbox = pygame.Rect(c1.x, c1.y + c1.idle_pose.get_height()-3 , c1.idle_pose.get_width(), 8)

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
        print(f"{c1.speed_y} 1")

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

        for platform in package_platforms:
            if c1_hitbox.colliderect(platform):
                if c1.speed_y > 0 and c1_hitbox.bottom <= platform.top + 5:
                    c1.y = platform.top - char_height
                    c1.speed_y = 0
                    c1.on_ground = True
    
        print(f"{c1.speed_y} 2")

        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True
        print(f"{c1.speed_y} 3")
        for p in platforms:
            screen.blit(p.image, p.rect)

        c1.update_animation(dt)
        screen.blit(c1.idle_pose, (c1.x, c1.y))
        #print(c1.y)
        print(package_platforms)
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
