from karel.stanfordkarel import *

def follow_beeper_path():
    """
    Moves Karel forward repeatedly as long as there is a beeper on its current corner.
    Assumes that there is a continuous path of beepers in front of Karel.
    """
    while beepers_present():
        move()

def main():
    """
    Starts Karel on a beeper path and follows it until the beeper path ends.
    """

    follow_beeper_path()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()