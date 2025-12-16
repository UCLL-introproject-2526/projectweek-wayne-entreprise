import pygame
import character
import package
import goal

def game_tuto():
    pygame.init()
    klok = pygame.time.Clock()
    pygame.display.set_caption("Kerst") 
    running = True

    background = pygame.image.load('Assets/dak.png')
    background = pygame.image.load('Assets/dak.png')
    background = pygame.transform.scale_by(background, 0.15625)
    screen = pygame.display.set_mode((320,320), pygame.FULLSCREEN | pygame.SCALED)

    c1 = character.Character((0, 160), 10)
    move_left = False
    move_right = False
    move_up=False

    font=pygame.font.Font(None,size=20)
    font_expl=pygame.font.Font(None,size=20)
    text=font.render('Level 0: Tutorial',True,(255,255,255))
    text_explain=font_expl.render(f'Press RIGHTARROW key: -> to go right',True,(255,255,255))
    text_explain2=font_expl.render(f'Press LEFTARROW key: <- to go left',True,(255,255,255))
    while running:
        screen.blit(background,(0,0))
        screen.blit(text,(100,20))
        screen.blit(text_explain,(20,50))
        screen.blit(text_explain2,(20,70))
        screen.blit(c1.idle_pose, (c1.x, c1.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    move_left = True
                    text_explain=font_expl.render('Press UP to jump',True,(255,255,255))
                    text_explain2=font_expl.render('',True,(255,255,255))
                if event.key == pygame.K_RIGHT:
                    move_right = True
                    text_explain=font_expl.render('Press UP to jump',True,(255,255,255))
                    text_explain2=font_expl.render('',True,(255,255,255))
                if event.key == pygame.K_UP:
                    move_up = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key==pygame.K_UP:
                    move_up = False
        
        if move_left:
            c1.move_left()
        elif move_right:
            c1.move_right()
        elif move_up:
            c1.move_up()
        else:
            ...



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