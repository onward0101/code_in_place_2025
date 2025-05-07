from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
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

def face_east():
    """
    Rotates karel until it is facing east.
    """
    while not_facing_east():
        turn_left()
    
def move_to_wall():
    """
    Continuously moves Karel forward until it is blocked by a wall.
    """
    while front_is_clear():
        move()

def repair_single_column():
    """
    Moves up a column, placing a beeper on each corner to repair it.
    After reaching the top, Karel returns to the bottom and faces east.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper() # Ensure the top is repaired
    turn_around()
    move_to_wall()
    face_east()

def move_to_next_column():
    """
    Moves Karel forward 4 spaces to reach the next column.
    """
    for _ in range(4):
        if front_is_clear():
            move()

def main():
    """
    Repairs all vertical columns by repeatedly moving to each one
    and calling the column repair function.
    """
    while front_is_clear():
        turn_left()
        repair_single_column()
        move_to_next_column()
    # Repair the final column when wall is ahead
    turn_left()
    repair_single_column()
    

if __name__ == '__main__':
    main()