def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        return None  # or raise ValueError("Input must be a dictionary")
    
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")
    
    dct[key] = value
    return dct

# Task 2

# Scenario 1: Add new key-value pair
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)  # Expected: {'name': 'Alice'}

# Scenario 2: Update existing key
result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2)  # Expected to print original value and return {'age': 26}
