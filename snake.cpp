#include <iostream>
#include <cstdlib> // For srand() and rand() functions
#include <ctime>   // For time() function
#include <unistd.h> // For usleep() function

using namespace std;

// Constants
const int WIDTH = 20;
const int HEIGHT = 20;
const char EMPTY = ' ';
const char SNAKE_BODY = 'O';
const char SNAKE_HEAD = '@';
const char FOOD = '*';

// Directions
enum Direction { UP, DOWN, LEFT, RIGHT };

// Game state
bool gameOver;
int score;
Direction dir;

// Snake coordinates
int snakeX[100], snakeY[100];
int snakeLength;

// Food coordinates
int foodX, foodY;

// Setup initial game state
void Setup() {
    gameOver = false;
    score = 0;
    dir = RIGHT;
    snakeX[0] = WIDTH / 2;
    snakeY[0] = HEIGHT / 2;
    snakeLength = 1;
    srand(time(0)); // Seed for random number generator
    foodX = rand() % WIDTH;
    foodY = rand() % HEIGHT;
}

// Draw game board
void Draw() {
    system("clear"); // Clear the console

    // Draw top border
    for (int i = 0; i < WIDTH + 2; i++) {
        cout << "#";
    }
    cout << endl;

    // Draw the board
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            if (x == 0)
                cout << "#"; // Draw left border

            if (x == foodX && y == foodY)
                cout << FOOD; // Draw food
            else if (x == snakeX[0] && y == snakeY[0])
                cout << SNAKE_HEAD; // Draw snake head
            else {
                bool print = false;
                for (int k = 1; k < snakeLength; k++) {
                    if (snakeX[k] == x && snakeY[k] == y) {
                        cout << SNAKE_BODY; // Draw snake body
                        print = true;
                    }
                }
                if (!print)
                    cout << EMPTY; // Draw empty space
            }

            if (x == WIDTH - 1)
                cout << "#"; // Draw right border
        }
        cout << endl;
    }

    // Draw bottom border
    for (int i = 0; i < WIDTH + 2; i++) {
        cout << "#";
    }
    cout << endl;

    // Display score
    cout << "Score: " << score << endl;
}

// Input handling
void Input() {
    char input;
    cin >> input;
    switch (input) {
        case 'w':
            dir = UP;
            break;
        case 's':
            dir = DOWN;
            break;
        case 'a':
            dir = LEFT;
            break;
        case 'd':
            dir = RIGHT;
            break;
        case 'x':
            gameOver = true;
            break;
    }
}

// Game logic
void Logic() {
    // Move the snake
    int prevX = snakeX[0];
    int prevY = snakeY[0];
    int prev2X, prev2Y;
    snakeX[0] = (dir == RIGHT) ? snakeX[0] + 1 : (dir == LEFT) ? snakeX[0] - 1 : snakeX[0];
    snakeY[0] = (dir == DOWN) ? snakeY[0] + 1 : (dir == UP) ? snakeY[0] - 1 : snakeY[0];

    // Check collision with borders
    if (snakeX[0] >= WIDTH || snakeX[0] < 0 || snakeY[0] >= HEIGHT || snakeY[0] < 0)
        gameOver = true;

    // Check collision with itself
    for (int i = 1; i < snakeLength; i++) {
        if (snakeX[0] == snakeX[i] && snakeY[0] == snakeY[i])
            gameOver = true;
    }

    // Eat food
    if (snakeX[0] == foodX && snakeY[0] == foodY) {
        score += 10;
        snakeLength++;
        foodX = rand() % WIDTH;
        foodY = rand() % HEIGHT;
    }

    // Move the rest of the snake
    for (int i = 1; i < snakeLength; i++) {
        prev2X = snakeX[i];
        prev2Y = snakeY[i];
        snakeX[i] = prevX;
        snakeY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }
}

int main() {
    Setup();

    while (!gameOver) {
        Draw();
        Input();
        Logic();
        usleep(100000); // Delay (100 milliseconds)
    }

    cout << "Game Over! Your final score is: " << score << endl;

    return 0;
}
