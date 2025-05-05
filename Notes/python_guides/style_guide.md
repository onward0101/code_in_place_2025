# Style Guide

## Descriptive Variable and Function name
### 1. Descriptive name: 
- specific and clear names make it easier for you to grasp the functionality of your program.
    ```py
    # Good
    def move_to_wall():
        …..

    # Bad
    def robot_moving():
        …..
    ```
### 2. Snake case: 
- lowercase letters and separating words with underscores
    ```py
    # Good
    def calculate_total_price(price, tax_rate):
        total_price = price * (1 + tax_rate)
        return total_price

    # Bad
    def CalculateTotalPrice(p, tr):
        x = p * (1 + tr)
        return x
    ```
### 3. Avoid Python Keywords as Names
- Python keywords that should not be used as function or variable names: False, True, None, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.

## Using Whitespace to Improve Code Readability
### 1. Use consistent indentation to show the hierarchy of your code blocks
### 2. Separate function definitions with two blank lines
### 3. Add a single blank line between logical sections within a function to group related lines of code together.
### 4. Surround operators with spaces to make expressions easier to read.

## Comments
### 1. Comment for each function
- Write a short comment for each function in your program to explain its purpose and how it works.
    ```py
    def calculate_area(radius):
        """Calculate the area of a circle given its radius."""
        area = 3.14 * radius ** 2
        return area
    ```

### 2. Comment at the top of each files 
- Describe its overall purpose and any important information about its contents
    ```py
    """
    Filename: geometry.py
    Author: Juliette
    Description: This module contains functions for calculating the area, perimeter, and volume of various geometric shapes.
    """
    …
    your_code_here
    …
    ```

### 3. Inline comments for complex code
- Avoid writing comments for straightforward code, as this can clutter your code and make it harder to read.
    ```py
    # Good
    def calculate_discount(price, discount_rate):
        if discount_rate <= 0.1:
            discount = price * discount_rate
        elif discount_rate <= 0.2:
            # Apply an additional 2% discount for rates between 10% and 20%
            discount = price * (discount_rate + 0.02)  
        else:
            discount = price * 0.25  # Maximum discount of 25%

        return discount

    # Some redundant / unnecessary comments
    def calculate_discount(price, discount_rate):
        if discount_rate <= 0.1:  # Check if discount rate is less than or equal to 10%
            discount = price * discount_rate  # Calculate discount
        elif discount_rate <= 0.2:  # Check if discount rate is less than or equal to 20%
            discount = price * (discount_rate + 0.02)  # Calculate discount with additional 2%
        else:  # Discount rate is greater than 20%
            discount = price * 0.25  # Calculate discount with maximum 25% rate

        return discount
    ```

## Decomposition
### 1. Do one thing 
### 2. Know what it does by looking at its name.
### 3. Less than 10 linesm 3 levels of indentation (not a strict rule)
### 4. Reusable and easy to modify

## Constants, Magic Numbers and Parameters
### Constants 
- constants are typically defined in upper snake case, which uses uppercase letters with words separated by underscores.
### Magic Numbers
- Magic numbers are hardcoded values that appear directly in your code without any explanation of their meaning or purpose
### Parameters
- Parameters are pieces of information that functions need to use when we call them. You can think of them as inputs to the function.

## Advanced style
### Typing Hints
- Use type hints to clarify inputs and outputs
```py
def calculate_total_price(price: float, tax_rate: float) -> float:
    return price * (1 + tax_rate)
```
### Docstring style 
```py
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return 3.14 * radius ** 2
```
### Line Length
- Code lines: ≤79 characters (≤88–100 if using modern tools like Black)

- Comments/docstrings: ≤72 characters

### Import Order
```py
import os
import sys # Standard library imports

import requests  # Third-party imports

from myapp.models import User # Local application imports
```

### Exception Handling
Catch specific exceptions, not broad "except"

## Reference 
1. Style guide: https://codeinplace.stanford.edu/cip3/textbook/style