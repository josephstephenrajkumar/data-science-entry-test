def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        return None  # or raise ValueError("Input must be a list")

    i = 0
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]
        i += 1

    return "No negatives"

# Task 2

# Scenario 1: list with negatives
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Result 1:", result1)  # Expected: -1

# Scenario 2: list with no negatives
result2 = find_first_negative([2, 10, 8, 0])
print("Result 2:", result2)  # Expected: "No negatives"
