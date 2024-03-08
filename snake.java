import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class SnakeGame extends JPanel implements KeyListener, ActionListener {
    // Constants
    private static final int WIDTH = 20;
    private static final int HEIGHT = 20;
    private static final int GRID_SIZE = 20;
    private static final int DELAY = 100; // Delay in milliseconds

    // Game state
    private boolean gameOver = false;
    private int score = 0;

    // Snake
    private ArrayList<Point> snake = new ArrayList<Point>();
    private int snakeLength = 3;
    private Point direction = new Point(1, 0); // Initial direction: right

    // Food
    private Point food = new Point();

    public SnakeGame() {
        setPreferredSize(new Dimension(WIDTH * GRID_SIZE, HEIGHT * GRID_SIZE));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);

        // Initialize snake position
        snake.add(new Point(10, 10));
        snake.add(new Point(9, 10));
        snake.add(new Point(8, 10));

        // Generate initial food position
        generateFood();

        // Start game loop
        Timer timer = new Timer(DELAY, this);
        timer.start();
    }

    // Generate random food position
    private void generateFood() {
        int x = (int) (Math.random() * WIDTH);
        int y = (int) (Math.random() * HEIGHT);
        food.setLocation(x, y);
    }

    // Draw game components
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw snake
        g.setColor(Color.GREEN);
        for (Point p : snake) {
            g.fillRect(p.x * GRID_SIZE, p.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
        }

        // Draw food
        g.setColor(Color.RED);
        g.fillRect(food.x * GRID_SIZE, food.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);

        // Draw score
        g.setColor(Color.WHITE);
        g.drawString("Score: " + score, 10, 20);

        // Draw game over message
        if (gameOver) {
            g.setColor(Color.WHITE);
            g.setFont(new Font("Arial", Font.BOLD, 24));
            String gameOverMsg = "Game Over! Final Score: " + score;
            int msgWidth = g.getFontMetrics().stringWidth(gameOverMsg);
            g.drawString(gameOverMsg, (WIDTH * GRID_SIZE - msgWidth) / 2, HEIGHT * GRID_SIZE / 
2);
        }
    }

    // Handle keyboard input
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if (key == KeyEvent.VK_UP && direction.y != 1) {
            direction.setLocation(0, -1);
        } else if (key == KeyEvent.VK_DOWN && direction.y != -1) {
            direction.setLocation(0, 1);
        } else if (key == KeyEvent.VK_LEFT && direction.x != 1) {
            direction.setLocation(-1, 0);
        } else if (key == KeyEvent.VK_RIGHT && direction.x != -1) {
            direction.setLocation(1, 0);
        }
    }

    // Unused KeyListener methods
    public void keyReleased(KeyEvent e) {}
    public void keyTyped(KeyEvent e) {}

    // Game loop
    public void actionPerformed(ActionEvent e) {
        if (!gameOver) {
            // Move snake
            Point head = snake.get(0);
            Point newHead = new Point(head.x + direction.x, head.y + direction.y);
            snake.add(0, newHead);

            // Check collision with food
            if (newHead.equals(food)) {
                generateFood();
                score += 10;
            } else {
                snake.remove(snake.size() - 1);
            }

            // Check collision with self or walls
            if (newHead.x < 0 || newHead.x >= WIDTH || newHead.y < 0 || newHead.y >= HEIGHT || 
snake.indexOf(newHead) != 0) {
                gameOver = true;
            }

            // Repaint
            repaint();
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Snake Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new SnakeGame());
        frame.pack();
        frame.setLocationRelativeTo(null); // Center the frame on the screen
        frame.setVisible(true);
    }
}

