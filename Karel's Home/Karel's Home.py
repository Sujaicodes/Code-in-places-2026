from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# move to the beeper, pick it up, and
# return home.
def main():
    move_to_package()
    pick_beeper()
    return_home()

# Helper function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Helper function to turn around
def turn_around():
    turn_left()
    turn_left()

# Function to navigate from start to the beeper
def move_to_package():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()

# Function to navigate back to the start and face original direction
def return_home():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
