from karel.stanfordkarel import *

def main():
    # Repair first column
    build_column()
    move_to_next_column()

    # Repair second column
    build_column()
    move_to_next_column()

    # Repair third column
    build_column()
    move_to_next_column()

    # Repair fourth column
    build_column()


def build_column():
    turn_left()

    # Repair bottom to top
    for i in range(4):
        if no_beepers_present():
            put_beeper()
        move()

    # Top corner
    if no_beepers_present():
        put_beeper()

    # Turn around
    turn_left()
    turn_left()

    # Come back down
    for i in range(4):
        move()

    # Face east again
    turn_left()


def move_to_next_column():
    for i in range(4):
        move()


if __name__ == '__main__':
    main()
