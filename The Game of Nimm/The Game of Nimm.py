def main():
    stones = 20
    player = 1

    while stones > 0:
        print("There are", stones, "stones left.")

        remove = int(input(
            "Player " + str(player) +
            " would you like to remove 1 or 2 stones? "
        ))

        while remove != 1 and remove != 2:
            remove = int(input("Please enter 1 or 2: "))

        stones -= remove
        print()

        # Switch players
        if player == 1:
            player = 2
        else:
            player = 1

    print("Player", player, "wins!")


if __name__ == '__main__':
    main()
