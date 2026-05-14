from graphics import Canvas

# Constants
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # --- Row 1 (Starter Code) ---
    # y-coordinate is 0 for the top row
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE * 2, 0)
    draw_circle_patch(canvas, PATCH_SIZE * 3, 0)
    
    # --- TODO: Milestone 2 (Second Row) ---
    # y-coordinate is PATCH_SIZE to shift everything down 100 pixels.
    # The pattern is swapped to alternating: Circle, Square, Circle, Square
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE * 2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE * 3, PATCH_SIZE)


# --- Patch Functions ---

def draw_square_patch(canvas, start_x, start_y):
    # Calculate the bottom right corner
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    
    # 1. Draw the outer purple square
    canvas.create_rectangle(start_x, start_y, end_x, end_y, "purple", "purple")
    
    # 2. Draw an inner white square to create the "frame"
    inset = 20  # The thickness of the frame
    canvas.create_rectangle(start_x + inset, start_y + inset, end_x - inset, end_y - inset, "white", "white")

# --- TODO: Milestone 1 (Circle Patch) ---
def draw_circle_patch(canvas, start_x, start_y):
    # Calculate the bottom right corner based on the starting position
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    
    # Draw the salmon circle inside the bounding box
    canvas.create_oval(start_x, start_y, end_x, end_y, "salmon", "salmon")


if __name__ == '__main__':
    main()
