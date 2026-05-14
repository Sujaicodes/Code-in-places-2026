from graphics import Canvas

# Constants provided in the assignment
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Outer loop: Iterate through each row (from base to top)
    for row in range(BRICKS_IN_BASE):
        
        # 1. Determine number of bricks in the current row
        bricks_in_row = BRICKS_IN_BASE - row
        
        # 2. Calculate the horizontal starting position to center the row
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        
        # 3. Calculate the vertical position (starting from the bottom)
        row_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        
        # Inner loop: Draw each individual brick in the current row
        for i in range(bricks_in_row):
            # Calculate coordinates for the current brick
            x1 = start_x + (i * BRICK_WIDTH)
            y1 = row_y
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            
            # Draw the brick on the canvas
            # Optional: Add 'yellow' as a parameter if you want to match the sample image exactly
            canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == '__main__':
    main()
