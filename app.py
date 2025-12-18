import pygame
import character
import package
import goal
import Platform
import Chimney
import Tutorial 
import Snowball
import sleigh


def main():
    pygame.init()
    music = pygame.mixer.Sound('Assets/sound/Chill Pulse - Jingle Bell Rock (freetouse.com).mp3') 
    music.play(-1)
    music.set_volume(0.1)
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
                if event.key == pygame.K_2:
                    game_loop(2) 
                    start = False
                if event.key == pygame.K_3:
                    game_loop(3) 
                    start = False
                if event.key == pygame.K_4:
                    game_loop(4) 
                    start = False
                if event.key == pygame.K_5:
                    game_loop(5) 
                    start = False
                if event.key == pygame.K_6:
                    game_loop(6) 
                    start = False
                if event.key == pygame.K_7:
                    game_loop(7) 
                    start = False
                if event.key == pygame.K_8:
                    game_loop(8) 
                    start = False
                if event.key == pygame.K_p:
                    running = False
                    Tutorial.game_tuto()
                    pygame.init()
                    music = pygame.mixer.Sound('Assets/sound/Chill Pulse - Jingle Bell Rock (freetouse.com).mp3') 
                    music.play(-1)
                    music.set_volume(0.1)
                    klok = pygame.time.Clock()
                    pygame.display.set_caption("Kerst") 
                    screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
                    start_image = pygame.image.load('Assets/start_background.png')
                    start_image = pygame.transform.scale_by(start_image, 0.5357142857)
                
        klok.tick(60)
        pygame.display.flip()
    running = True
    
    if start: 
        game_loop(1)

def game_loop(start_level):
    end_game = False
    level = start_level
    while not end_game:
        klok = pygame.time.Clock()
        screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
        running = True
        loop2 = True
        loop3 = True

        #reset level values
        platforms = []
        chimneys = []
        packages = 0
        flag_coordinates = flag_x, flag_y = (-100,0)
        start_coordinates = (0,0)
        sled_coordinates = (-100,0)
        sled_packages = 0
        snowballs = []


        start_image = pygame.image.load('Assets/affiche.webp')
        start_image = pygame.transform.scale_by(start_image, 0.5357142857)

        if level == 1:
            flag_coordinates = flag_x, flag_y = (330, 305)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 2
            platforms = [
            Platform.Platform(230, 400, 64, 32),
            Platform.Platform(300, 350, 64, 32)
            ]
            sled_coordinates = (600, 450)
            sled_packages = 3
        if level == 2:
            flag_coordinates = flag_x, flag_y = (280, 105)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 5
            platforms = [
            Platform.Platform(250, 400, 64, 32),
            Platform.Platform(320, 300, 64, 32),
            Platform.Platform(250, 150, 64, 32),
            ]
        if level == 3:
            flag_coordinates = flag_x, flag_y = (380, 55)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 5
            chimneys=[Chimney.Chimney(200,screen.get_height()*3/4-170,100,140),
                Chimney.Chimney(400,screen.get_height()*3/4-180,100,150),
                Chimney.Chimney(610,screen.get_height()*3/4-180,100,150)
                ]
            platforms = [
            Platform.Platform(350, 100, 64, 32),
            Platform.Platform(450, 200, 64, 32),
            Platform.Platform(600, 250, 64, 32)
            ]
            snowballs=[Snowball.Snowball(300,0,50,50)]
        if level == 4:
            flag_coordinates = flag_x, flag_y = (620, 315)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 3
            chimneys=[Chimney.Chimney(250,screen.get_height()*3/4-170,100,140),
                Chimney.Chimney(600,screen.get_height()*3/4-180,130,160)
                ]
            platforms = [
            Platform.Platform(200, 300, 64, 32),
            Platform.Platform(350, 250, 64, 32),
            Platform.Platform(500, 200, 64, 32)
            ]
        if level == 5:
            flag_coordinates = flag_x, flag_y = (650, 105)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 4
            chimneys=[Chimney.Chimney(150,screen.get_height()*3/4-170,100,140),
                Chimney.Chimney(350,screen.get_height()*3/4-180,130,160)
                ]
            platforms = [
            Platform.Platform(200, 300, 64, 32),
            Platform.Platform(400, 250, 64, 32),
            Platform.Platform(600, 150, 64, 32)
            ]
        if level == 6:
            flag_coordinates = flag_x, flag_y = (660, screen.get_height()*3/4-80)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 1
            chimneys=[Chimney.Chimney(150,screen.get_height()*3/4-170,100,140),
                      Chimney.Chimney(500,screen.get_height()*3/4-230,130,200)
                ]
            platforms = [
            Platform.Platform(80, 440, 64, 32),
            Platform.Platform(250, 350, 64, 32),
            ]
        if level == 7:
            flag_coordinates = flag_x, flag_y = (660, screen.get_height()*3/4-85)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 0
            chimneys=[Chimney.Chimney(150,screen.get_height()*3/4-170,100,140),
                      Chimney.Chimney(500,screen.get_height()*3/4-230,130,200)
                ]
            platforms = [
            Platform.Platform(80, 440, 64, 32),
            Platform.Platform(250, 350, 64, 32),
            ]


        background = pygame.image.load('Assets/dak.png')
        background = pygame.transform.scale_by(background, 0.351568)

        flag=pygame.image.load('Assets/flag/Flag_18x32.png')
        flag=pygame.transform.scale_by(flag,1.5)

        c1 = character.Character(start_coordinates, packages)
        c1.on_ground = False

        sled = sleigh.Sleigh(sled_packages, sled_coordinates)
        
        char_width = c1.idle_pose.get_width()
        
        g1 = goal.Goal(screen)
        move_left = False
        move_right = False

        flag_hitbox = pygame.Rect(flag_x - 15, flag_y, flag.get_width() + 15, flag.get_height())
        font=pygame.font.Font(None,size=30)
        text=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))

        while running and loop2:
            dt = klok.tick(60)    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    end_game = True
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        end_game = True
                    if event.key == pygame.K_LEFT:
                        move_left = True
                        c1.set_direction(False)
                        c1.set_direction(False)
                    if event.key == pygame.K_RIGHT:
                        move_right = True
                        c1.set_direction(True)
                        c1.set_direction(True)
                    if event.key == pygame.K_SPACE:
                        #print(c1.get_total_packages())
                        if c1_hitbox.colliderect(flag_hitbox) and c1.get_total_packages()>0:
                                loop2 = g1.win()
                        c1.place_package(all_objects)
                        text=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                        
                    if event.key == pygame.K_UP:
                        c1.jump()
                    if event.key == pygame.K_r:
                        c1.x = start_x
                        c1.y = start_y
                        c1.clean_packages()
                        c1.set_total_packages_left(packages)
                        sled.reset()
                        text=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                    
                    

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        move_left = False
                    if event.key == pygame.K_RIGHT:
                        move_right = False

            if move_left and c1.x>0:
                c1.move_left()
            if move_right and c1.x<screen.get_width()-char_width:
                c1.move_right()

            c1.playerfalling(dt)

            if not c1.on_ground:
                c1.on_ground = False
            c1_hitbox = pygame.Rect(c1.x+6, c1.y + c1.idle_pose.get_height()-3 , 18, 8)

            screen.blit(background, (0,0))
            screen.blit(flag, flag_coordinates)
            screen.blit(text,(300,20))

            floor_y = screen.get_height() * 3//4 - 30
            char_height = c1.idle_pose.get_height()
            
            for p in platforms:
                if c1_hitbox.colliderect(p.rect):
                    if c1.speed_y > 0 and c1_hitbox.bottom < p.rect.bottom:
                        c1.y = p.rect.top - char_height 
                        c1.speed_y = 0                  
                        c1.on_ground = True
            for hitbox in chimneys:
                if c1_hitbox.colliderect(hitbox.rect):
                #print(f"c1:{c1_hitbox.right}")
                #print(f"hitbox:{hitbox.left}")
                    if c1.speed_y >= 0 and c1_hitbox.bottom < hitbox.rect.top+20:
                        c1.y = hitbox.rect.top - char_height 
                        c1.speed_y = 0                  
                        c1.on_ground = True

                    elif c1_hitbox.centerx < hitbox.rect.centerx:
                        c1.x = hitbox.rect.left-char_width
                        #print(hitbox.right-char_width)
                        #print(c1.x)

                    elif c1_hitbox.centerx > hitbox.rect.centerx:
                        c1.x = hitbox.rect.right
            for snowball in snowballs:
                if c1_hitbox.colliderect(snowball.rect):
                    c1.speed_y=0.1
                    c1.on_ground = False

            

            
            # Package collision detection
            for pkg in c1.package_list:
                screen.blit(pkg.image, (pkg.x, pkg.y))
                if not pkg.freeze:
                    pkg.package_falling(dt, platforms=platforms, Chimneys=chimneys)
            
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
            
            
            all_objects = [*package_platforms,*platforms,*chimneys]
            
            for platform in package_platforms:
                if c1_hitbox.colliderect(platform):
                    if c1.speed_y > 0 and c1_hitbox.bottom <= platform.bottom + 5:
                        c1.y = platform.top - char_height +1
                        c1.speed_y = 0
                        c1.on_ground = True

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
            for chimney in chimneys:
                screen.blit(chimney.image, chimney.rect) 
            for snowball in snowballs:
                snowball.Snowball_fall(dt) 
                screen.blit(snowball.image, snowball.rect)   

            c1.update_animation(dt)
            screen.blit(c1.idle_pose, (c1.x, c1.y))
           
            screen.blit(sled.image, sled.rect)
            if c1_hitbox.colliderect(sled.rect):
                if sled.used == False:
                    c1.set_total_packages_left(sled.refill())
                    text=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))

            pygame.display.flip()
            
        
        if level == 10:
            g1.win()
            while running and loop3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        end_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            end_game = True
                klok.tick(60)
            end_game = True 
        level += 1


main()
