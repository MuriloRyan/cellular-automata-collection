import pygame
from conway import Grid

pygame.init()

screen_width, screen_height = 640, 480
fullscreen = False
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Game of Life")

size_x, size_y = 256, 256
grid = Grid().generate_grid(size_x, size_y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # update windowed size
            screen_width, screen_height = event.w, event.h
            if not fullscreen:
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            # toggle fullscreen with F11
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    screen_width, screen_height = screen.get_size()
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    surface = screen
    surface.fill((0, 0, 0))  # Clear the screen once per frame

    # compute cell size to fit the current window
    cell_w = max(1, surface.get_width() // size_x)
    cell_h = max(1, surface.get_height() // size_y)
    cell_size = min(cell_w, cell_h)

    grid_width = cell_size * size_x
    grid_height = cell_size * size_y
    offset_x = (surface.get_width() - grid_width) // 2
    offset_y = (surface.get_height() - grid_height) // 2

    for x in range(size_x):
        for y in range(size_y):
            if grid.grid[x][y] == 1:
                pygame.draw.rect(
                    surface,
                    (255, 255, 255),
                    (
                        offset_x + x * cell_size,
                        offset_y + y * cell_size,
                        cell_size,
                        cell_size,
                    ),
                )

    grid.update_grid()
    pygame.display.flip()