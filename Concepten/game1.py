import pygame
pygame.init()
screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
running=True
santa=pygame.image.load('Concepten/santa_claus_improved.png').convert_alpha()
santa=pygame.transform.scale(santa,(santa.get_width()//10,santa.get_height()//10))
background=pygame.image.load('Concepten/background.png')
background=pygame.transform.scale(background,(background.get_width()/2,background.get_height()/2))

positionx_santax=0
positiony_santax=screen.get_height()/2
horizontal_axis=screen.get_height()/2
clock=pygame.time.Clock()
delta_time=0.1
font=pygame.font.Font(None,size=30)

while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    screen.blit(santa,(positionx_santax,positiony_santax))
    hitbox_santa=pygame.Rect(positionx_santax,positiony_santax,santa.get_width()-5,santa.get_height()-5)
    target=pygame.Rect(300,santa.get_height()+200,160,200)
    #hitbox_target=pygame.Rect(300,)

    text=font.render('Level 0!',True,(255,255,255))
    screen.blit(text,(100,20))

    move_x=0
    move_y=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #if event.type==pygame.KEYUP:
         #   if event.key==pygame.K_RIGHT:
          #      move_x+=10*delta_time*100
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key==pygame.K_RIGHT:
                move_x+=20
            if event.key==pygame.K_LEFT:
                move_x-=20
            if event.key==pygame.K_SPACE:
                move_y+=50
            if event.key==pygame.K_DOWN:
                move_y-=10
            if event.key==pygame.K_UP:
                move_y+=50
    if positionx_santax==0 and move_x<=0:
        positiony_santax-=move_y
    elif collision!=True:
        positionx_santax+=move_x
        positiony_santax-=move_y
    elif collision!=False and move_x<=0 and move_y>=0:
        positionx_santax+=move_x
        positiony_santax-=move_y
    # or positionx_santax<target.get_

    collision=hitbox_santa.colliderect(target)
    pygame.draw.rect(screen,(255*collision,255,0),target)
    #gravity
    if collision!=True :
        positiony_santax+=20*delta_time

    if horizontal_axis<positiony_santax:
        positiony_santax=horizontal_axis

    pygame.display.flip()
    delta_time=clock.tick(30)
    delta_time=max(0.001,min(0.1,delta_time))

pygame.quit()
