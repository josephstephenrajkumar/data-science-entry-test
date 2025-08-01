def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return None  # or raise ValueError("Input must be a string")
    
    return s[::-1]  # Slicing to reverse the string

# Task 2
# Scenario 1
result1 = string_reverse("Tariffs are hurting Singapore")
print("Result 1:", result1)  # Expected: "dlroW olleH"

# Scenario 2
result2 = string_reverse("Data Science and Machine Learning")
print("Result 2:", result2)  # Expected: "nohtyP"
