import pygame
import character
import package
import goal
import Chimney


def game_tuto():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    running = True
    startscreen=True
    endscreen=True
    start=pygame.image.load('Assets/affiche.webp')
    start = pygame.transform.scale_by(start, 0.5357142857)
    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.351568)
    screen = pygame.display.set_mode((720,720), pygame.FULLSCREEN | pygame.SCALED)
    screen2= pygame.display.set_mode((720,720), pygame.FULLSCREEN | pygame.SCALED)
    chimneys=[Chimney.Chimney(400,screen.get_height()*3/4-180,100,150),Chimney.Chimney(610,screen.get_height()*3/4-180,100,150)]
    flag=pygame.image.load('Assets/flag/Flag_18x32.png')
    flag=pygame.transform.scale_by(flag,1.5)

    #empty list of obsticles
    obstacles=[]

    ###
    while startscreen:
        screen.blit(start, (0,154))
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
        

    c1 = character.Character((0, 400), 6)
    c1.on_ground=False
    move_left = False
    move_right = False
    aantal_packages=c1.get_total_packages()
    font=pygame.font.Font(None,size=30)
    font_expl=pygame.font.Font(None,size=50)
    text=font.render('Level 0: Tutorial',True,(255,255,255))
    packages_left=font.render(f'Total amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
    text_explain=font_expl.render(f'Press RIGHTARROW key: -> to go right',True,(255,255,255))
    text_explain2=font_expl.render(f'Press LEFTARROW key: <- to go left',True,(255,255,255))
    text_explain3=font_expl.render(f'Congrats you just completed the tutorial',True,(255,255,255))
    floor=screen.get_height()*3/4-30
    messageshow1=True
    messageshow2=True

    g1 = goal.Goal(screen)

    while running:
        dt = klok.tick(60)  
        screen.blit(background,(0,0))
        screen.blit(flag,(655,320))
        screen.blit(text,(100,20))
        screen.blit(packages_left,(300,20))
        screen.blit(text_explain,(15,50))
        screen.blit(text_explain2,(15,80))
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
                    if messageshow1:
                        text_explain=font_expl.render('Press UP to jump',True,(255,255,255))
                        text_explain2=font_expl.render('',True,(255,255,255))
                        messageshow1=False
                if event.key == pygame.K_RIGHT:
                    if c1.x<screen.get_width():
                        move_right = True
                    if messageshow1:
                        text_explain=font_expl.render('Press UP to jump',True,(255,255,255))
                        text_explain2=font_expl.render('',True,(255,255,255))
                        messageshow1=False
                if event.key == pygame.K_UP:
                    c1.jump()
                    if messageshow2:
                        text_explain=font_expl.render('The Goal of this game is simple',True,(255,255,255))
                        text_explain2=font_expl.render('Try to deliver the package to the flag',True,(255,255,255))
                if event.key == pygame.K_SPACE:
                    c1.place_package()
                    packages_left=font.render(f'Total amount of packages left:{c1.get_total_packages()}',True,(255,255,255))
                    if c1_hitbox.colliderect(flag_hitbox):
                        text_explain=font_expl.render('',True,(255,255,255))
                        text_explain2=font_expl.render('',True,(255,255,255))
                        screen.blit(text_explain,(20,50))
                        screen.blit(text_explain2,(20,80))
                        print("check this")
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
        #hitboxen
        flag_hitbox=pygame.Rect(655,320,flag.get_width(),flag.get_height())
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
        #collision1=c1_hitbox.colliderect(shimney1_hitbox)
        hitbox_floor=pygame.Rect(0,screen.get_height()*3/4,screen.get_width(),screen.get_height()*1/4)
        ###""
        floor_y = screen.get_height() * 3/4-30
        if c1.x>300 and c1.x<500 and running:
            messageshow2=False
            text_explain=font_expl.render('Place packages by pressing space to go up',True,(255,255,255))
            text_explain2=font_expl.render('',True,(255,255,255))
        elif c1.x>500 and running:
            text_explain=font_expl.render('When close to the flag press space',True,(255,255,255))
            text_explain2=font_expl.render('to drop a package',True,(255,255,255))

        ###        
        
        #
        for hitbox in chimneys:
            if c1_hitbox.colliderect(hitbox.rect):
                #print(f"c1:{c1_hitbox.right}")
                #print(f"hitbox:{hitbox.left}")
                if c1.speed_y > 0 and c1_hitbox.bottom < hitbox.rect.top+20:
                    c1.y = hitbox.rect.top - char_height 
                    c1.speed_y = 0                  
                    c1.on_ground = True
                elif c1_hitbox.centerx < hitbox.rect.centerx:
                    print("check1")
                    c1.x = hitbox.rect.left-char_width
                    #print(hitbox.right-char_width)
                    #print(c1.x)
                elif c1_hitbox.centerx > hitbox.rect.centerx:
                    print("check2")
                    c1.x = hitbox.rect.right
        for pkg in c1.package_list:
            screen.blit(pkg.image, (pkg.x, pkg.y))
            pkg.package_falling(dt)
        
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
        
        
        all_objects = [*package_platforms,*chimneys]
        
        for platform in package_platforms:
            if c1_hitbox.colliderect(platform):
                if c1.speed_y > 0 and c1_hitbox.bottom <= platform.top + 5:
                    c1.y = platform.top - char_height +1
                    c1.speed_y = 0
                    c1.on_ground = True
                # print("touching")
        
        touching_object = None
        for obj in all_objects:
            if c1_hitbox.colliderect(obj):
                touching_object = True


        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True 
        for chimney in chimneys:
            screen.blit(chimney.image, chimney.rect)  

        klok.tick(60)
        pygame.display.flip()

    while endscreen:
        screen2.fill((0,0,0))
        screen2.blit(text_explain3,(20,80))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endscreen = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endscreen = False
                if event.key == pygame.K_SPACE:
                    endscreen = False
        klok.tick(60)
        pygame.display.flip()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        klok.tick(60)
    pygame.quit()

game_tuto()