def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap without using temporary variables (Pythonic)
    x, y = y, x
    print(f"x = {x}, y = {y}")

    # End of SWAP function


# Scenario 1: Non-numeric input
result1 = swap("NTU", 1)
if result1 == -1:
    print("Non-numeric input detected.")

# Scenario 2: Valid numeric input
result2 = swap(20, 15)
if result2 == -1:
    print("Non-numeric input detected.")
