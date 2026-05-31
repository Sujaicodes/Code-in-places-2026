from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # ==========================================
    # Milestone #1: Set up the World
    # ==========================================
    # Player starts top-left (0, 0), goal starts at (360, 360)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, "red")
    
    # Store the current direction of travel. 
    # Starts by moving RIGHT (x changes by 20, y changes by 0)
    velocity_x = SIZE
    velocity_y = 0
    
    # animation loop
    while True:
        # ==========================================
        # Milestone #3: Handle Key Press
        # ==========================================
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            velocity_x = -SIZE
            velocity_y = 0
        elif key == 'ArrowRight':
            velocity_x = SIZE
            velocity_y = 0
        elif key == 'ArrowUp':
            velocity_x = 0
            velocity_y = -SIZE
        elif key == 'ArrowDown':
            velocity_x = 0
            velocity_y = SIZE
            
        # ==========================================
        # Milestone #2: Animate
        # ==========================================
        canvas.move(player, velocity_x, velocity_y)
        
        # Get the current coordinates for collisions
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        
        # ==========================================
        # Milestone #4: Detecting collisions
        # ==========================================
        # If the player hits the edge of the canvas, the game ends
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            print("Game Over! You hit the wall.")
            break 
            
        # ==========================================
        # Milestone #5: Moving the goal
        # ==========================================
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        
        # Check if the top-left corners of both squares match
        if player_x == goal_x and player_y == goal_y:
            # Calculate a random coordinate that is a multiple of 20
            # E.g., for a 400px canvas, valid multipliers are 0 through 19
            max_multiplier_x = (CANVAS_WIDTH // SIZE) - 1
            max_multiplier_y = (CANVAS_HEIGHT // SIZE) - 1
            
            new_goal_x = random.randint(0, max_multiplier_x) * SIZE
            new_goal_y = random.randint(0, max_multiplier_y) * SIZE
            
            # Move the goal to the newly generated coordinates
            canvas.moveto(goal, new_goal_x, new_goal_y)
            
        # sleep
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
