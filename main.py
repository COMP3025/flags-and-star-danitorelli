import pygame
import sys
import math
from pygame.locals import QUIT

def draw_star(screen, position, size, angle):
    center_x, center_y = position
    
    star_vertices = [
        (center_x, center_y - 50 * size),
        (center_x + 15 * size, center_y - 20 * size),
        (center_x + 50 * size, center_y - 20 * size),
        (center_x + 20 * size, center_y + 10 * size),
        (center_x + 35 * size, center_y + 50 * size),
        (center_x, center_y + 30 * size),
        (center_x - 35 * size, center_y + 50 * size),
        (center_x - 20 * size, center_y + 10 * size),
        (center_x - 50 * size, center_y - 20 * size),
        (center_x - 15 * size, center_y - 20 * size),
    ]
    
    rotated_star = []
    for vertex in star_vertices:
        x = center_x + (vertex[0] - center_x) * math.cos(angle) - (vertex[1] - center_y) * math.sin(angle)
        y = center_y + (vertex[0] - center_x) * math.sin(angle) + (vertex[1] - center_y) * math.cos(angle)
        rotated_star.append((x, y))
    
    pygame.draw.polygon(screen, (255, 255, 255), rotated_star, 0)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 500))


while True:
    DISPLAYSURF.fill((0, 0, 0))
    
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (200, 150, 300, 100))
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (200, 150, 300, 20))
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (200, 190, 300, 20))
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (200, 230, 300, 20))
    
    triangle_vertices = ((200, 150), (300, 200), (200, 250))
    
    center_x = sum(vertex[0] for vertex in triangle_vertices) / 3
    center_y = sum(vertex[1] for vertex in triangle_vertices) / 3
    
    scale_factor = 0.3
    
    pygame.draw.polygon(DISPLAYSURF, (0, 0, 255), triangle_vertices, 0)
    draw_star(DISPLAYSURF, (center_x, center_y), scale_factor, 0)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
