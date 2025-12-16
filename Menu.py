import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

button_width = 200
button_height = 80
button_rect = pygame.Rect(0, 0, button_width, button_height)
button_rect.center = (WIDTH // 2, HEIGHT // 2)

button_color = (0, 200, 0)
hover_color = (0, 255, 0)
text_color = (255, 255, 255)
bg_color = (30, 30, 30)

def main():
    running = True
    while running:
        screen.fill(bg_color)
        
        mouse_pos = pygame.mouse.get_pos()
        
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        text_surf = font.render("START", True, text_color)
        text_rect = text_surf.get_rect(center=button_rect.center)
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Start button clicked")
                    # logic to start game goes here

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()