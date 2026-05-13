from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# Pick up all the beepers in the first row.

def main():
    while front_is_clear():
        pick_all_beepers()
        move()

    # Pick beepers at the last position
    pick_all_beepers()


def pick_all_beepers():
    while beepers_present():
        pick_beeper()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
