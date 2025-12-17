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
    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.351568)
    shimney1=pygame.image.load('Assets/shimney.png')
    shimney1=pygame.transform.scale_by(shimney1,0.04)
    shimney2=pygame.image.load('Assets/shimney.png')
    shimney2=pygame.transform.scale_by(shimney2,0.04)
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
    move_up=False

    font=pygame.font.Font(None,size=30)
    font_expl=pygame.font.Font(None,size=50)
    text=font.render('Level 0: Tutorial',True,(255,255,255))
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

        screen.blit(shimney1,(350,screen.get_height()*3/4-60))
        screen.blit(shimney2,(600,screen.get_height()*3/4-60))
        screen.blit(flag,(630,screen.get_height()*3/4-100))
        screen.blit(text,(100,20))
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
                    move_up = True
                    if messageshow2:
                        text_explain=font_expl.render('The Goal of this game is simple',True,(255,255,255))
                        text_explain2=font_expl.render('Try to deliver the package to the flag',True,(255,255,255))



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key==pygame.K_UP:
                    move_up = False
        
        if move_left and c1.x>0 and (not collision1 and not after):
            c1.move_left()
        elif move_right and c1.x<background.get_width() and (not collision1 and not before):
            c1.move_right()
        elif move_up:
            c1.move_up()
        else:
            ...
        #hitboxen
        shimney1_hitbox=pygame.Rect(350,screen.get_height()*3/4-60,shimney1.get_width(),shimney1.get_height())
        obstacles.append(shimney1_hitbox)
        c1_hitbox = pygame.Rect(c1.x, c1.y, c1.idle_pose.get_width(), c1.idle_pose.get_height())
        collision1=c1_hitbox.colliderect(shimney1_hitbox)
        hitbox_floor=pygame.Rect(0,screen.get_height()*3/4,screen.get_width(),screen.get_height()*1/4)
        ###""
        if c1_hitbox.colliderect(hitbox_floor) and collision1!=True:
            c1.y = hitbox_floor.top - c1.idle_pose.get_height()
            c1.speed_y = 0
        elif collision1==True and above:
            c1.y=shimney1_hitbox.top
        ###
        tollerance=10
        if collision1:
            if abs(c1_hitbox.right-shimney1_hitbox.left)<tollerance:
                print(1)
                before=True
            else:
                before=False
            if abs(c1_hitbox.left-shimney1_hitbox.right)<tollerance:
                print(2)
                after=True
            else:
                after=False
            if abs(c1_hitbox.top-shimney1_hitbox.bottom)<tollerance:
                print(3)
                above=True
            else:
                above=False
                

        c1.playerfalling(dt)

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