from graphics import Canvas
import time

# We set the radius to 20, meaning the ball is 40x40 pixels total
BALL_RADIUS = 20

def main():
    # 1. Set up the canvas
    canvas = Canvas()
    
    # 2. Initialize the blue ball
    # We draw it starting at top-left (0,0) and bottom-right (40, 40)
    ball = canvas.create_oval(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2, "blue")
    
    # The mouse tracking loop
    while True:
        # Get the current mouse coordinates
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # Shift the coordinates so the mouse is in the middle of the ball
        new_x = mouse_x - BALL_RADIUS
        new_y = mouse_y - BALL_RADIUS
        
        # Move the ball to the new offset coordinates
        canvas.moveto(ball, new_x, new_y)
        
        # Pause briefly to allow the canvas to render the frame
        time.sleep(0.02)

if __name__ == '__main__':
    main()
