from karel.stanfordkarel import *

def main():
    # Keep moving while the current corner has a beeper
    while beepers_present():
        move()

    # Karel is now on the first empty corner
    # Move one more step to reach home
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
