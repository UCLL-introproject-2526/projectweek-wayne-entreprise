import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((1040, 600))
pygame.display.set_caption("Star Wars")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
background_color = (255, 0, 0)

# Background
background = pygame.image.load("background_starwars.jpg")

# X-wing
x_wingImg = pygame.image.load("x-wing.png")
x_wing_x = 450
x_wing_y = 425
x_wing_x_change = 0  # Movement of x-wing

# Tie Fighter
speed_tie = 3

def create_tie():
    return [random.randint(140, 900), random.randint(50, 150), speed_tie if random.random() > 0.5 else -speed_tie, 80]

tie_fighters = [create_tie()]

tie_fighterImg = pygame.image.load("tie_fighter_4.png")

# Laser
laserImg = pygame.image.load("laser.png")
x_laser = 0
y_laser = 480
laser_state = "ready"
laser_state_right = "ready"

# Score
score_value = 0
x_score = 10
y_score = 10
font = pygame.font.Font('freesansbold.ttf', 32)

# Explosion
kaboomImg = pygame.image.load("kaboom.png")
kaboom_x = 0
kaboom_y = 0
show_kaboom = False
kaboom_timer = 0

# Laser Speed
y_laser_change = 5

# Functions
def x_wing(x, y):
    screen.blit(x_wingImg, (x, y))

def tie_fighter(x, y):
    screen.blit(tie_fighterImg, (x, y))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def iscollision(x_enemy, y_enemy, x_bullet, y_bullet):
    distance = math.sqrt((math.pow(x_enemy - x_bullet, 2)) + (math.pow(y_enemy - y_bullet, 2)))
    return distance < 140

#fire left laser
def fire_laser_left(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x+0,y-90))

#fire right laser
#def fire_laser_right(x,y):
    #global laser_state_right
    #laser_state_right = "fire"
    #screen.blit(laserImg, (x+125,y-90))

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(background_color)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                x_wing_x_change = -2.5
            if event.key == pygame.K_RIGHT:
                x_wing_x_change = 2.5
            if event.key == pygame.K_UP and laser_state == "ready":
                x_laser = x_wing_x
                fire_laser_left(x_laser, y_laser)
                #fire_laser_right(x_laser, y_laser)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                x_wing_x_change = 0

    x_wing_x += x_wing_x_change
    x_wing_x = max(0, min(x_wing_x, 900))

    for tie in tie_fighters[:]:
        tie[0] += tie[2]
        if tie[0] <= 0 or tie[0] >= 900:
            tie[2] *= -1
            tie[1] += tie[3]

        if iscollision(tie[0], tie[1], x_laser, y_laser):
            y_laser = 480
            laser_state = "ready"
            score_value += 1
            kaboom_x, kaboom_y = tie[0], tie[1]
            show_kaboom = True
            kaboom_timer = pygame.time.get_ticks()
            tie_fighters.remove(tie)
            tie_fighters.append(create_tie())
            tie_fighters.append(create_tie())

        tie_fighter(tie[0], tie[1])

    if laser_state == "fire":
        #fire_laser_right(x_laser, y_laser)
        fire_laser_left(x_laser, y_laser)
        y_laser -= y_laser_change
        if y_laser <= 0:
            y_laser = 480
            laser_state = "ready"

    if show_kaboom:
        screen.blit(kaboomImg, (kaboom_x, kaboom_y))
        if pygame.time.get_ticks() - kaboom_timer > 500:
            show_kaboom = False

    x_wing(x_wing_x, x_wing_y)
    show_score(x_score, y_score)

    pygame.display.flip()
    clock.tick(200)

pygame.quit()
