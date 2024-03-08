import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
UP = (0, -1)  # Moving up means decreasing the Y coordinate
DOWN = (0, 1)  # Moving down means increasing the Y coordinate
LEFT = (-1, 0)  # Moving left means decreasing the X coordinate
RIGHT = (1, 0)  # Moving right means increasing the X coordinate


# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        # Starting position of the snake in the middle of the screen
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        # Snake's initial direction is random
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        # Snake's color
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    # Change snake's direction based on user input
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # Move the snake
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        # Calculate new position based on current direction
        new = (
            ((cur[0] + (x * GRID_SIZE)) % WIDTH),
            (cur[1] + (y * GRID_SIZE)) % HEIGHT,
        )
        # Check for collisions with itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()  # Reset the game if the snake collides with itself
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Reset the snake to its initial state
    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Draw the snake on the screen
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    # Handle user input to change snake's direction
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        # Place the food at a random position on the screen
        self.randomize_position()

    # Randomize food position
    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    # Draw the food on the screen
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)


# Main function
def main():
    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")  # Set the window title
    clock = pygame.time.Clock()

    # Create instances of Snake and Food classes
    snake = Snake()
    food = Food()

    # Main game loop
    while True:
        screen.fill(BLACK)  # Fill the screen with black color
        snake.handle_keys()  # Handle user input to control the snake
        snake.move()  # Move the snake
        # Check if the snake eats the food
        if snake.get_head_position() == food.position:
            snake.length += 1  # Increase snake's length
            food.randomize_position()  # Move the food to a new random position
        snake.draw(screen)  # Draw the snake on the screen
        food.draw(screen)  # Draw the food on the screen
        pygame.display.update()  # Update the display
        clock.tick(10)  # Control the game's frame rate


# Run the game
if __name__ == "__main__":
    main()
