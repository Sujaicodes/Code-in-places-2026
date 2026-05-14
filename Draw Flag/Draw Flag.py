from graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate the exact middle of the canvas height
    mid_y = CANVAS_HEIGHT / 2
    
    # Draw the top red rectangle
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, mid_y, "red")

if __name__ == '__main__':
    main()
