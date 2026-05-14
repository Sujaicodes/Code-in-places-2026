from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate the fixed Y coordinates for the bottom row
    top_y = CANVAS_HEIGHT - BOX_SIZE
    bottom_y = CANVAS_HEIGHT
    
    # Loop 5 times to create the 5 boxes
    for i in range(N_BOXES):
        left_x = i * BOX_SIZE
        right_x = left_x + BOX_SIZE
        
        canvas.create_rectangle(
            left_x, 
            top_y, 
            right_x, 
            bottom_y, 
            "white", 
            "black"
        )

if __name__ == '__main__':
    main()
