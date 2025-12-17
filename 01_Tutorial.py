import pygame
import character
import package
import goal

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
    shimney1=pygame.image.load('Assets/Chimney/chimney_26x31.png')
    shimney1=pygame.transform.scale_by(shimney1,2)
    shimney2=pygame.image.load('Assets/Chimney/chimney_26x31.png')
    shimney2=pygame.transform.scale_by(shimney2,2)
    flag=pygame.image.load('Assets/flag/Flag_18x32.png')
    flag=pygame.transform.scale_by(flag,1.5)
    screen = pygame.display.set_mode((720,720), pygame.FULLSCREEN | pygame.SCALED)
    #empty list of obsticles
    obstacles=[]

    ###
    while startscreen:
        screen.blit(start,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    startscreen=False
        klok.tick(60)
        pygame.display.flip() 
        

    c1 = character.Character((0, 160), 10)
    move_left = False
    move_right = False
    aantal_packages=1
    font=pygame.font.Font(None,size=30)
    font_expl=pygame.font.Font(None,size=50)
    text=font.render('Level 0: Tutorial',True,(255,255,255))
    packages_left=font.render(f'Total amount of packages left:{aantal_packages}',True,(255,255,255))
    text_explain=font_expl.render(f'Press RIGHTARROW key: -> to go right',True,(255,255,255))
    text_explain2=font_expl.render(f'Press LEFTARROW key: <- to go left',True,(255,255,255))
    
    messageshow1=True
    messageshow2=True
    before=False
    after=False
    above=False

    while running:
        dt = klok.tick(60)  
        screen.blit(background,(0,0))
        screen.blit(shimney1,(350,screen.get_height()*3/4-50))
        screen.blit(shimney2,(600,screen.get_height()*3/4-50))
        screen.blit(flag,(630,screen.get_height()*3/4-100))
        screen.blit(text,(100,20))
        screen.blit(packages_left,(300,20))
        screen.blit(text_explain,(20,50))
        screen.blit(text_explain2,(20,80))
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
        c1.playerfalling(dt)
        #hitboxen
        hitboxen=[]
        shimney1_hitbox=pygame.Rect(350,screen.get_height()*3/4-50,shimney1.get_width(),shimney1.get_height())
        shimney2_hitbox=pygame.Rect(600,screen.get_height()*3/4-50,shimney2.get_width(),shimney2.get_height())
        hitboxen.append(shimney1_hitbox)
        hitboxen.append(shimney2_hitbox)
        obstacles.append(shimney1_hitbox)
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
        collision1=c1_hitbox.colliderect(shimney1_hitbox)
        hitbox_floor=pygame.Rect(0,screen.get_height()*3/4,screen.get_width(),screen.get_height()*1/4)
        ###""
        char_height = c1.idle_pose.get_height()
        char_width = c1.idle_pose.get_width()
        floor_y = screen.get_height() * 3/4
        if c1.x>500:
            messageshow2=False
            text_explain=font_expl.render('When close to the flag press space',True,(255,255,255))
            text_explain2=font_expl.render('to drop a package',True,(255,255,255))

        ###
        if c1.y + char_height >= floor_y:
            c1.y = floor_y - char_height  
            c1.speed_y = 0                
            c1.on_ground = True           
        else:
            c1.on_ground = False
        
        #
        for hitbox in hitboxen:
            if c1_hitbox.colliderect(hitbox):
                #print(f"c1:{c1_hitbox.right}")
                #print(f"hitbox:{hitbox.left}")
                if c1.speed_y > 0 and c1_hitbox.bottom < hitbox.bottom:
                    c1.y = hitbox.top - char_height 
                    c1.speed_y = 0                  
                    c1.on_ground = True
                elif c1_hitbox.right>hitbox.left and c1_hitbox.right<hitbox.right-char_width:
                    print("check1")
                    c1.x = hitbox.left-char_width
                    print(hitbox.right-char_width)
                    print(c1.x)
                elif c1_hitbox.left<hitbox.right  and c1_hitbox.left>hitbox.left:
                    print("check2")
                    c1.x = hitbox.right

        

        

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