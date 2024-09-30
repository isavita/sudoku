import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 2
THICK_LINE_WIDTH = 4
NUMBER_FONT = pygame.font.SysFont('arial', 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def generate_puzzle():
    # For simplicity, we'll use a predefined complete Sudoku board and remove some numbers
    # In a real scenario, you'd implement a Sudoku generator
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    # Remove numbers to create the puzzle (keep most empty)
    # Let's remove 50 numbers randomly
    attempts = 50
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1
    return board

# Initialize the board
sudoku_board = generate_puzzle()

def draw_grid():
    for i in range(GRID_SIZE + 1):
        line_width = THICK_LINE_WIDTH if i % 3 == 0 else LINE_WIDTH
        
        # Draw vertical lines
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), line_width)
        
        # Draw horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)

def draw_numbers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            number = sudoku_board[row][col]
            if number != 0:
                text = NUMBER_FONT.render(str(number), True, BLUE)
                text_rect = text.get_rect(center=((col + 0.5) * CELL_SIZE, (row + 0.5) * CELL_SIZE))
                screen.blit(text, text_rect)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        pygame.display.flip()

if __name__ == "__main__":
    print("Starting Sudoku game...")
    main()
