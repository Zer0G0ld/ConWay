import pygame

pygame.init()

BLACK = (0,0,0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 255)

WIDTH, HEIGHT = 600, 600
TILE_SIZE = 2
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (5 * TILE_SIZE))

def main():
    running = True

    positions = set()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                running = False

    screen.fill(GREY)
    draw_grid(positions)
    pygame.quit()
    pygame.display.update()

if __name__ == "__main__":
    main()