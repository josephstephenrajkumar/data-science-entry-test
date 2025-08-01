def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return None  # or raise ValueError("Input must be a list")
    
    return [replace_val if item == find_val else item for item in lst]

# Task 2
# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Result 1:", result1)  # Expected: [1, 5, 3, 4, 5, 5]

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Result 2:", result2)  # Expected: ["orange", "banana", "orange"]

