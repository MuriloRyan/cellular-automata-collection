import pygame
from briansbrain import BrainsBrain

pygame.init()

screen_width, screen_height = 1280, 720
fullscreen = False

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brians Brain")

clock = pygame.time.Clock()

size_x, size_y = 256, 256
cell_size = 2
grid = BrainsBrain(width = size_x, height = size_y)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

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

    grid.update_grid()

    surface.fill((0, 0, 0))  # Clear the screen once per frame

    for x in range(size_x):
        for y in range(size_y):
            _x, _y = x * cell_size,y * cell_size
            cell = pygame.Rect(_x,_y,cell_size,cell_size)

            if grid.grid[x][y] == 1:
                pygame.draw.rect(surface,WHITE, cell)

            elif grid.grid[x][y] == 2:
                pygame.draw.rect(surface,GRAY, cell)

            elif grid.grid[x][y] == 0:
                continue

    
    pygame.display.flip()
    clock.tick()
    fps = clock.get_fps()
    pygame.display.set_caption(f"Brians Brain - FPS: {clock.get_fps():.1f}")