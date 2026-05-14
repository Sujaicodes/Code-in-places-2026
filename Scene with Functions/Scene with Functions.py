from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # 1. Draw the background (Sky and Ground)
    draw_background(canvas)
    
    # 2. Draw a Sun
    # x, y, radius, color
    draw_sun(canvas, 500, 80, 50, "gold")
    
    # 3. Draw Mountains in the background
    # x, bottom_y, width, height, color
    draw_mountain(canvas, -50, 300, 300, 200, "slategray")
    draw_mountain(canvas, 150, 300, 400, 280, "lightslategray")
    draw_mountain(canvas, 400, 300, 250, 150, "slategray")
    
    # 4. Draw Clouds
    # x, y, width, height
    draw_cloud(canvas, 50, 50, 120, 40)
    draw_cloud(canvas, 250, 80, 150, 50)
    draw_cloud(canvas, 450, 40, 100, 30)
    
    # 5. Draw Trees
    # x, y, trunk_width, trunk_height
    draw_tree(canvas, 50, 220, 20, 80)
    draw_tree(canvas, 150, 250, 15, 50)
    draw_tree(canvas, 450, 200, 30, 100)
    
    # 6. Draw Birds (The custom new object)
    # x, y
    draw_bird(canvas, 200, 120)
    draw_bird(canvas, 230, 100)
    draw_bird(canvas, 260, 130)


# --- Reusable Scene Functions ---

def draw_background(canvas):
    # Sky
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "lightskyblue", "lightskyblue")
    
    # Ground (Starts 300 pixels down and goes to the bottom)
    canvas.create_rectangle(0, 300, CANVAS_WIDTH, CANVAS_HEIGHT, "forestgreen", "forestgreen")

def draw_sun(canvas, center_x, center_y, radius, color):
    # Calculate the bounding box for the oval using the center coordinates and radius
    left_x = center_x - radius
    top_y = center_y - radius
    right_x = center_x + radius
    bottom_y = center_y + radius
    
    canvas.create_oval(left_x, top_y, right_x, bottom_y, color, color)

def draw_cloud(canvas, x, y, width, height):
    # A cloud made of three overlapping ovals
    canvas.create_oval(x, y, x + width*0.6, y + height, "white", "white")
    canvas.create_oval(x + width*0.2, y - height*0.4, x + width*0.8, y + height*0.9, "white", "white")
    canvas.create_oval(x + width*0.4, y, x + width, y + height, "white", "white")

def draw_mountain(canvas, x, bottom_y, width, height, color):
    # A simple triangular mountain using a polygon
    # The three points are: bottom-left, top-center, bottom-right
    canvas.create_polygon(
        x, bottom_y, 
        x + width/2, bottom_y - height, 
        x + width, bottom_y, 
        color, "black"
    )

def draw_tree(canvas, x, y, trunk_width, trunk_height):
    # Draw the brown trunk
    canvas.create_rectangle(x, y, x + trunk_width, y + trunk_height, "saddlebrown", "saddlebrown")
    
    # Draw the green leafy top
    leaves_radius = trunk_width * 1.5
    leaves_x = x + (trunk_width / 2) - leaves_radius
    leaves_y = y - leaves_radius
    
    canvas.create_oval(
        leaves_x, leaves_y, 
        leaves_x + leaves_radius*2, leaves_y + leaves_radius*2, 
        "mediumseagreen", "darkgreen"
    )

def draw_bird(canvas, x, y):
    # A simple "V" shape for a bird using two lines
    canvas.create_line(x, y, x + 10, y + 10, "black")
    canvas.create_line(x + 10, y + 10, x + 20, y, "black")

if __name__ == '__main__':
    main()
