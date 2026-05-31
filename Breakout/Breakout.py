from graphics import Canvas
import time
import random

# --- Constants (Update these if your starter code has different ones) ---
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600

# Brick constants
N_ROWS = 10
N_COLS = 10
BRICK_SPACING = 4
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS + 1) * BRICK_SPACING) / N_COLS
BRICK_HEIGHT = 10
BRICK_START_Y = 50

# Paddle constants
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
PADDLE_Y_OFFSET = 30

# Ball constants
BALL_RADIUS = 10
BALL_SIZE = BALL_RADIUS * 2
DELAY = 0.02
TURNS = 3

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Milestone 1: Create Bricks
    total_bricks = create_bricks(canvas)
    
    # Milestone 3: Create Paddle
    paddle_y = CANVAS_HEIGHT - PADDLE_Y_OFFSET
    paddle = canvas.create_rectangle(
        (CANVAS_WIDTH - PADDLE_WIDTH) / 2, 
        paddle_y, 
        (CANVAS_WIDTH + PADDLE_WIDTH) / 2, 
        paddle_y + PADDLE_HEIGHT, 
        "black"
    )
    
    # Milestone 5: Play 3 Turns
    for turn in range(TURNS):
        print(f"Turn {turn + 1} begins!")
        
        # Milestone 2: Create Ball
        ball = canvas.create_oval(
            CANVAS_WIDTH/2 - BALL_RADIUS, CANVAS_HEIGHT/2 - BALL_RADIUS,
            CANVAS_WIDTH/2 + BALL_RADIUS, CANVAS_HEIGHT/2 + BALL_RADIUS,
            "black"
        )
        
        # Set initial velocity
        change_x = random.uniform(3, 5)
        if random.random() < 0.5:
            change_x = -change_x
        change_y = 5.0
        
        # Animation Loop for a single turn
        while True:
            # Move the paddle to track the mouse (keeping it on screen)
            mouse_x = canvas.get_mouse_x()
            new_paddle_x = mouse_x - (PADDLE_WIDTH / 2)
            # Ensure paddle doesn't go off the left or right edges
            if new_paddle_x < 0:
                new_paddle_x = 0
            elif new_paddle_x > CANVAS_WIDTH - PADDLE_WIDTH:
                new_paddle_x = CANVAS_WIDTH - PADDLE_WIDTH
            canvas.moveto(paddle, new_paddle_x, paddle_y)
            
            # Move the ball
            canvas.move(ball, change_x, change_y)
            ball_x = canvas.get_left_x(ball)
            ball_y = canvas.get_top_y(ball)
            
            # Wall Collisions (Left/Right)
            if ball_x <= 0 or ball_x + BALL_SIZE >= CANVAS_WIDTH:
                change_x = -change_x
            
            # Wall Collision (Top)
            if ball_y <= 0:
                change_y = -change_y
                
            # Wall Collision (Bottom) -> Lose turn
            if ball_y + BALL_SIZE >= CANVAS_HEIGHT:
                print("You missed!")
                canvas.delete(ball)
                break 
                
            # Milestone 4: Check for Object Collisions
            colliders = canvas.find_overlapping(ball_x, ball_y, ball_x + BALL_SIZE, ball_y + BALL_SIZE)
            
            for collider in colliders:
                if collider != ball:
                    # If it hits the paddle
                    if collider == paddle:
                        # Fix for the "glue bug": strictly enforce upward movement
                        change_y = -abs(change_y)
                    # If it hits a brick
                    else:
                        canvas.delete(collider)
                        change_y = -change_y
                        total_bricks -= 1
                    break # Only handle one collision per frame
            
            # Win Condition
            if total_bricks == 0:
                print("You Win!")
                return # Exits the whole game immediately
                
            time.sleep(DELAY)
            
    print("Game Over. No turns left!")

def create_bricks(canvas):
    """
    Draws the bricks and returns the total number of bricks created.
    """
    colors = ["red", "orange", "yellow", "green", "cyan"]
    
    # Calculate starting X to perfectly center the grid
    grid_width = (N_COLS * BRICK_WIDTH) + ((N_COLS - 1) * BRICK_SPACING)
    start_x = (CANVAS_WIDTH - grid_width) / 2
    
    bricks_created = 0
    
    for row in range(N_ROWS):
        # Every 2 rows, change the color
        color_index = (row // 2) % len(colors)
        color = colors[color_index]
        
        for col in range(N_COLS):
            x = start_x + col * (BRICK_WIDTH + BRICK_SPACING)
            y = BRICK_START_Y + row * (BRICK_HEIGHT + BRICK_SPACING)
            
            canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, color)
            bricks_created += 1
            
    return bricks_created

if __name__ == '__main__':
    main()
