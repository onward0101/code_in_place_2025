from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def move_to_beeper():
    """
    Moves Karel forward until it reaches a beeper.
    """
    while no_beepers_present():
        move()

def place_puzzle_beeper():
    """
    Executes Hardcoded movements to place a beeper in the puzzle.
    """
    move()
    turn_left()
    move()
    move()
    put_beeper()

def turn_around():
    """
    Turns Karel 180 degrees to face the opposite direction.
    """
    turn_left()
    turn_left()

def turn_right():
    """
    Turns Karel 90 degrees to the right.
    """
    turn_left()
    turn_left()
    turn_left()

def move_to_wall():
    """
    Continuously moves Karel forward until it is blocked by a wall.
    """
    while front_is_clear():
        move()

def face_east():
    """
    Rotates the karel until it is facing east.
    """
    while not_facing_east():
        turn_left()

def return_home():
    """
    Executes hardcoded movements to return Karel to the bottom-left corner.
    """
    turn_around()
    move_to_wall()
    turn_right()
    move_to_wall()
    face_east()

def main():
    move_to_beeper()
    pick_beeper()
    put_the_puzzle()
    return_home()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()