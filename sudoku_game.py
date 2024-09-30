import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 2
THICK_LINE_WIDTH = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_grid():
    for i in range(GRID_SIZE + 1):
        line_width = THICK_LINE_WIDTH if i % 3 == 0 else LINE_WIDTH
        
        # Draw vertical lines
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), line_width)
        
        # Draw horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()

if __name__ == "__main__":
    print("Sudoku")
    print(f"Width: {WIDTH}")
    print(f"Height: {HEIGHT}")
    print(f"Grid Size: {GRID_SIZE}")
    print(f"Cell Size: {CELL_SIZE}")
    print(f"Line Width: {LINE_WIDTH}")
    print(f"Thick Line Width: {THICK_LINE_WIDTH}")
    main()
