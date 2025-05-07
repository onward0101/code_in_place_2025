from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def turn_right():
    """
    Turns Karel 90 degrees to the right.
    """
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """
    Turns Karel 180 degrees to face the opposite direction.
    """
    turn_left()
    turn_left()
    
def move_to_wall():
    """
    Continuously moves Karel forward until it is blocked by a wall.
    """
    while front_is_clear():
        move()

def fill_one_row_with_beepers():
    """
    Moves karel forward, placing a beeper on each corner until it is blocked by a wall.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def forward_next_row():
    """
    Adjusts the direction of karel and moves it forward to the next row.
    """
    turn_right()
    move()
    turn_right()

def main():
    """
    Fills every row in the world with beepers by zigzagging through the grid.
    """
    while left_is_clear():
        fill_one_row_with_beepers()
        turn_around()
        move_to_wall()
        forward_next_row()
    fill_one_row_with_beepers() # Fill the top row.


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()