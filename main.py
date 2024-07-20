import pygame
import math
import sys

from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Raycasting')
clock = pygame.time.Clock()

def draw_map():
    for row in range(8):
        for col in range(8):
            # calculate square index
            square = row * MAP_SIZE + col
            
            # draw map in the game window
            pygame.draw.rect(
                screen,
                (200, 200, 200) if MAP[square] == '#' else (100, 100, 100),
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 2, TILE_SIZE - 2)
            )

    pygame.draw.circle(screen, (255, 0, 0), (int(player_x), int(player_y)), 8)

    # draw player direction
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y),
                                       (player_x - math.sin(player_angle) * 50,
                                        player_y + math.cos(player_angle) * 50), 2)
    
    # draw player FOV
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y),
                                       (player_x - math.sin(player_angle - HALF_FOV) * 50,
                                        player_y + math.cos(player_angle - HALF_FOV) * 50), 2)
    
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y),
                                       (player_x - math.sin(player_angle + HALF_FOV) * 50,
                                        player_y + math.cos(player_angle + HALF_FOV) * 50), 2)

def raycasting():
    start_angle = player_angle - HALF_FOV

    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y + math.cos(start_angle) * depth

            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)

            square = row * MAP_SIZE + col

            if MAP[square] == '#':
                # highlight wall that has been hit by a casted ray
                pygame.draw.rect(screen, (0, 255, 0), (col * TILE_SIZE,
                                                    row * TILE_SIZE,
                                                    TILE_SIZE - 2,
                                                    TILE_SIZE - 2))

                pygame.draw.line(screen, (255, 255, 0), (player_x, player_y), (target_x, target_y))

                color = 255 / (1 + depth * depth * 0.0001)
                
                # fix fish eye effect
                depth *= math.cos(player_angle - start_angle)
                                
                wall_height = 21000 / (depth + 0.0001)
                
                # fix stuck at the wall
                if wall_height > SCREEN_HEIGHT: wall_height = SCREEN_HEIGHT 
                
                # draw 3D projection
                pygame.draw.rect(screen, (color, color, color), (
                    SCREEN_HEIGHT + ray * SCALE,
                    (SCREEN_HEIGHT / 2) - wall_height / 2,
                     SCALE, wall_height))

                break

        start_angle += STEP_ANGLE

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SCREEN_COLOR)
    draw_map()
    raycasting()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: player_angle -= 0.1
    if keys[pygame.K_RIGHT]: player_angle += 0.1
    if keys[pygame.K_UP]:
        player_x += -math.sin(player_angle) * 4
        player_y += math.cos(player_angle) * 4
    if keys[pygame.K_DOWN]:
        player_x -= -math.sin(player_angle) * 4
        player_y -= math.cos(player_angle) * 4

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()