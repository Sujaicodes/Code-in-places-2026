from karel.stanfordkarel import *

def main():
    build_step_one()
    move_to_next_step()

    build_step_two()
    move_to_next_step()

    build_step_three()
    move_to_next_step()

    build_step_four()


def build_step_one():
    put_beeper()


def build_step_two():
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_left()


def build_step_three():
    put_beeper()

    turn_left()
    move()
    put_beeper()

    move()
    put_beeper()

    turn_around()
    move()
    move()
    turn_left()


def build_step_four():
    put_beeper()

    turn_left()
    move()
    put_beeper()

    move()
    put_beeper()

    move()
    put_beeper()

    turn_around()
    move()
    move()
    move()
    turn_left()


def move_to_next_step():
    for i in range(2):
        move()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
