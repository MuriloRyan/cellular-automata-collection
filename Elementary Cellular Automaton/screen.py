# Generated with ChatGPT since I dont even know how a camera works in a 2D game
#  I just want to see the damn cellular automaton in action

from eca import ElementaryCA
import pygame

# =========================
# CONFIG
# =========================

WIDTH = 800
HEIGHT = 600

FPS = 60
GENERATIONS_PER_SECOND = 120

BACKGROUND = (0, 0, 0)
FOREGROUND = (255, 255, 255)

seed = '00000010001000000000000000000000000000000000000000000000000000000010'
rule = 'rule110'

ca = ElementaryCA(
    rule,
    size=800,  # Set size to match screen width for better visualization
    seed=seed
)

# =========================
# AUTO CELL SIZE
# =========================

CELL_SIZE = max(1, WIDTH // ca.size)

# =========================
# INIT
# =========================

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elementary Cellular Automaton")

clock = pygame.time.Clock()

seed = '0000001000000' # Seed: string of '0' and '1' characters representing the initial state; change to see different patterns
rule = 'rule110'

ca = ElementaryCA(rule , seed=seed)

camera_y = 0
auto_follow = True  # Start with auto-follow enabled

generation_timer = 0

running = True

# =========================
# MAIN LOOP
# =========================

while running:
    dt = clock.tick(FPS) / 1000.0

    # -------------------------
    # INPUT
    # -------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                auto_follow = not auto_follow  # Toggle auto-follow with spacebar

    keys = pygame.key.get_pressed()

    scroll_speed = 500 * dt

    if not auto_follow:
        if keys[pygame.K_UP]:
            camera_y -= scroll_speed

        if keys[pygame.K_DOWN]:
            camera_y += scroll_speed

    # -------------------------
    # UPDATE
    # -------------------------

    generation_timer += dt

    if generation_timer >= (1 / GENERATIONS_PER_SECOND):
        ca.generate()
        generation_timer = 0

    # camera auto-follows
    # compute max camera based on number of generations (rows) in the CA
    max_camera = max(
        0,
        len(ca.states) * CELL_SIZE - HEIGHT
    )

    if auto_follow:
        camera_y = max_camera

    # Clamp camera_y to valid range
    camera_y = max(0, min(camera_y, max_camera))

    # -------------------------
    # RENDER
    # -------------------------

    screen.fill(BACKGROUND)

    for y, state in enumerate(ca.states):

        screen_y = y * CELL_SIZE - camera_y

        # culling vertical
        if screen_y < -CELL_SIZE:
            continue

        if screen_y > HEIGHT:
            break

        for x, cell in enumerate(state):

            if not cell:
                continue

            pygame.draw.rect(
                screen,
                FOREGROUND,
                (
                    x * CELL_SIZE,
                    screen_y,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

    pygame.display.flip()

pygame.quit()