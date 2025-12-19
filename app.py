import pygame
import character
import package
import goal
import Platform
import Chimney
import Tutorial 
import Snowball
import sleigh
import random


def main():
    pygame.init()
    song1 = pygame.mixer.Sound('Assets/sound/Epic Spectrum - Feliz Navidad (freetouse.com).mp3') 
    song2 = pygame.mixer.Sound('Assets/sound/Epic Spectrum - Happy New Year (freetouse.com).mp3')
    song3 = pygame.mixer.Sound('Assets/sound/Epic Spectrum - Last Christmas (freetouse.com).mp3')
    song4 = pygame.mixer.Sound('Assets/sound/Chill Pulse - Jingle Bell Rock (freetouse.com).mp3')
    music = [song1, song2, song3, song4]
    mn = random.randint(0,2)
    print(mn)
    music[mn].play(-1)
    music[mn].set_volume(0.1)
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    screen = pygame.display.set_mode((720, 720), pygame.FULLSCREEN | pygame.SCALED)
    start_image = pygame.image.load('Assets/start_background.png')
    start_image = pygame.transform.scale_by(start_image, 0.26470588235294117647058823529412)
    start = True
    running = True
    while start and running:
        screen.blit(start_image, (0,154))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    start = False
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
        jump_packages = 0
        flag_coordinates = flag_x, flag_y = (-100,0)
        start_coordinates = (0,0)
        sled_coordinates = (-100,0)
        sled_packages = 0
        sled_special_packages = 0
        snowballs = []


        start_image = pygame.image.load('Assets/affiche.webp')
        start_image = pygame.transform.scale_by(start_image, 0.5357142857)
        sleigh_is_there=False

        if level == 1:
            flag_coordinates = flag_x, flag_y = (330, 305)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 2
            jump_packages = 2
            platforms = [
            Platform.Platform(230, 400, 64, 32),
            Platform.Platform(300, 350, 64, 32)
            ]
            sled_coordinates = (600, 450)
            sled_packages = 3
            sled_special_packages = 2
            sleigh_is_there=True
        if level == 2:
            flag_coordinates = flag_x, flag_y = (280, 105)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 5
            jump_packages = 4
            platforms = [
            Platform.Platform(250, 400, 64, 32),
            Platform.Platform(320, 300, 64, 32),
            Platform.Platform(250, 150, 64, 32),
            ]
            sleigh_is_there=False
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
            snowballs=[Snowball.Snowball(300,0,50,50,0.001),
                       Snowball.Snowball(500,0,50,50,0.001)]
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
            Platform.Platform(280, 350, 64, 32),
            ]
        if level == 7:
            flag_coordinates = flag_x, flag_y = (695, 55)
            start_coordinates = start_x, start_y = (20, 400)
            packages = 2
            chimneys=[Chimney.Chimney(100,screen.get_height()*3/4-175,100,145),
            ]
            platforms = [
            Platform.Platform(350, 350, 50, 20),
            Platform.Platform(500, 350, 50, 20),
            Platform.Platform(650, 350, 64, 32),
            Platform.Platform(50, 200, 64, 32),
            Platform.Platform(50, 100, 64, 32),
            Platform.Platform(200, 100, 64, 32),
            Platform.Platform(350, 100, 50, 20),
            Platform.Platform(500, 100, 50, 20),
            Platform.Platform(650, 100, 64, 32),
            ]
            snowballs=[Snowball.Snowball(300,-50,50,50,0.010),
                       Snowball.Snowball(425,-50,50,50,0.075),
                       Snowball.Snowball(575,-50,50,50,0.125),
                       Snowball.Snowball(425,-350,50,50,0.075),
                       Snowball.Snowball(575,-800,50,50,0.5),
                       Snowball.Snowball(425,-500,50,50,0.075),
                       Snowball.Snowball(575,-1200,50,50,0.5),
                       Snowball.Snowball(575,-1400,50,50,0.5),
                       Snowball.Snowball(575,-1600,50,50,0.5),
                       Snowball.Snowball(575,-1800,50,50,0.5),
                       Snowball.Snowball(575,-2000,50,50,0.5),
                       Snowball.Snowball(575,-2200,50,50,0.5),
                       Snowball.Snowball(575,-2400,50,50,0.5),
                       Snowball.Snowball(575,-2600,50,50,0.5),
                       Snowball.Snowball(575,-2800,50,50,0.5),
                       Snowball.Snowball(575,-3000,50,50,0.5),
                       ]
            sled_coordinates = (650, 325)
            sled_packages = 4
            sleigh_is_there=True
        if level==8:
            flag_coordinates = flag_x, flag_y = (695, 55)
            start_coordinates = start_x, start_y = (250, 400)
            packages = 0
            chimneys=[Chimney.Chimney(100,screen.get_height()*3/4-300,150,300),
                      Chimney.Chimney(350,screen.get_height()*3/4-350,150,350)
            ]
            jump_packages = 2
            platforms = [
            Platform.Platform(200, 350, 64, 32),
            Platform.Platform(-10, 325, 64, 32),
            Platform.Platform(685, 100, 20, 15)]
            snowballs=[Snowball.Snowball(50,-200,50,50,0.9),
                       Snowball.Snowball(610,-225,50,50,0.9)]
            sled_coordinates = (-5, 300)
            sled_packages = 4
            sleigh_is_there=True
            


        background = pygame.image.load('Assets/dak.png')
        background = pygame.transform.scale_by(background, 0.351568)

        flag=pygame.image.load('Assets/flag/Flag_18x32.png')
        flag=pygame.transform.scale_by(flag,1.5)

        c1 = character.Character(start_coordinates, packages)
        c1.on_ground = False

        sled = sleigh.Sleigh(sled_packages,sled_special_packages, sled_coordinates)
        
        #set jump packages
        c1.set_jump_pack(jump_packages)

        char_width = c1.idle_pose.get_width()
        
        g1 = goal.Goal(screen)
        move_left = False
        move_right = False

        flag_hitbox = pygame.Rect(flag_x - 15, flag_y, flag.get_width() + 15, flag.get_height())
        font=pygame.font.Font(None,size=30)
        font2=pygame.font.Font(None,size=60)       
        text1=font.render(f'Level:{level}',True,(255,255,255))
        text2=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
        text3=font2.render('',True,(255,255,255))
        text_jump_pack = font.render(f'Boost Packages left:{c1.placeable_jump_pack}',True,(255,0,0))
        text_change_pkg1 = font.render(f'\'C\' to switch',True,(255,255,0))
        text_placing_normal = font.render(f'Now placing: Normal',True,(255,255,0))
        text_placing_jump = font.render(f'Now placing: Jump',True,(255,255,0))

        

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
                    if event.key == pygame.K_RIGHT:
                        move_right = True
                        c1.set_direction(True)
                    if event.key == pygame.K_SPACE:
                        #print(c1.get_total_packages())
                        if c1_hitbox.colliderect(flag_hitbox) and c1.get_total_packages()>0:
                                loop2 = g1.win()
                        if c1.get_total_packages()==0:
                            if sleigh_is_there:
                                text3=font.render(f'No more packages left press R to restart or use the sledge perhaps?',True,(255,255,255))
                            else:
                                text3=font.render(f'No more packages left press R to restart',True,(255,255,255))
                        c1.place_package(all_objects)
                        if c1.placeable_jump_pack == 0:
                            c1.place_type = 0
                        text2=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                    if event.key == pygame.K_c:
                        c1.change_place_type()

                    if event.key == pygame.K_UP:
                        c1.jump(-0.35)
                    if event.key == pygame.K_r:
                        c1.x = start_x
                        c1.y = start_y
                        c1.clean_packages()
                        c1.set_total_packages_left(packages)
                        c1.set_jump_pack(jump_packages)
                        c1.place_type = 0
                        sled.reset()
                    

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


            text_jump_pack = font.render(f'Boost Packages left:{c1.placeable_jump_pack}',True,(255,0,0))

            screen.blit(background, (0,0))
            screen.blit(flag, flag_coordinates)
            screen.blit(text1,(40,20))
            screen.blit(text2,(420,20))
            if c1.placeable_jump_pack > 0:
                screen.blit(text_jump_pack,(420,40))
                screen.blit(text_change_pkg1, (40, 40))
                if c1.place_type == 0 :
                    screen.blit(text_placing_normal,(40,60))
                else:
                    screen.blit(text_placing_jump,(40,60))


            floor_y = screen.get_height() * 3//4 - 30
            char_height = c1.idle_pose.get_height()
            
            for p in platforms:
                if c1_hitbox.colliderect(p.rect):
                    if c1.speed_y > 0 and c1_hitbox.bottom < p.rect.bottom:
                        c1.y = p.rect.top - char_height 
                        c1.speed_y = 0                  
                        c1.on_ground = True
            for chimney in chimneys:
                if c1_hitbox.colliderect(chimney.hitbox):
                #print(f"c1:{c1_hitbox.right}")
                #print(f"hitbox:{hitbox.left}")
                    if c1.speed_y >= 0 and c1_hitbox.bottom < chimney.hitbox.top+20:
                        c1.y = chimney.hitbox.top - char_height 
                        c1.speed_y = 0                  
                        c1.on_ground = True

                    elif c1_hitbox.centerx < chimney.hitbox.centerx:
                        c1.x = chimney.hitbox.left-char_width
                        #print(hitbox.right-char_width)
                        #print(c1.x)

                    elif c1_hitbox.centerx > chimney.hitbox.centerx:
                        c1.x = chimney.hitbox.right
            for snowball in snowballs:
                if c1_hitbox.colliderect(snowball.rect):
                    c1.speed_y=0.3
                    c1.on_ground = False

            

            
            # Package collision detection
            for pkg in c1.package_list:
                screen.blit(pkg.image, (pkg.x, pkg.y))
                if not pkg.freeze:
                    pkg.package_falling(dt, platforms=platforms, Chimneys=chimneys)
                
            
            package_platforms = []
            booster_list = []

            for pkg1 in c1.package_list:
                pkg_rect_upper_own = None
                pkg_rect_lower_own = pkg1.get_rect_lower()
                if pkg1.type == 1:
                    pkg_rect_boost = pkg1.get_rect_upper()
                else:
                    pkg_rect_upper_own = pkg1.get_rect_upper()

                for pkg2 in c1.package_list:
                    if pkg1 is pkg2:
                        continue 
                    pkg_rect_upper = pkg2.get_rect_upper()
                    if pkg_rect_lower_own.colliderect(pkg_rect_upper):
                        pkg1.y = pkg_rect_upper.top - 48
                        pkg1.freeze = True
                if pkg1.freeze:
                    if pkg1.type == 1:
                        package_platforms.append(pkg_rect_boost)
                        booster_list.append(pkg_rect_boost)
                    else:
                        package_platforms.append(pkg_rect_upper_own)
            
            
            all_objects = [*package_platforms,*platforms,*chimneys]
            
            for platform in package_platforms:
                if c1_hitbox.colliderect(platform):
                    if platform in booster_list:
                        c1.speed_y = 0
                        c1.speed_y = -0.5
                        c1.on_ground = False
                    if platform in all_objects and not platform in booster_list:
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
            pygame.display.flip()  
        
           
            screen.blit(sled.image, sled.rect)
            if c1_hitbox.colliderect(sled.rect):
                if sled.used == False:
                    c1.set_total_packages_left(sled.refill())
                    c1.set_jump_pack(sled.refill_special())
            text2=font.render(f'Amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                    

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
