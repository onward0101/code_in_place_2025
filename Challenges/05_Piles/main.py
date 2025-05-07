from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    # Moves Karel forward through the world, picking up all beepers along the way.
    while front_is_clear():
        move()
        while beepers_present():
            pick_beeper()
        move()
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()