show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Step 1: Normalize the string
    # Convert to lowercase and filter out non-alphanumeric characters
    normalized = ''.join(char.lower() for char in teststr if char.isalnum())
    
    # Step 2: Check if the string is a palindrome
    # Compare the normalized string with its reverse
    is_palindrome = normalized == normalized[::-1]
    
    # Step 3: Return the result
    return is_palindrome

# This is how your code will be called.
# Your function should return whether a string is a palindrome.
# The code will count the number of correct answers
total = 0
test_words = ["Hello World!", "Radar", "Mama?", "Madam, I'm Adam.", "Race car!"]
for word in test_words:
    total += Answer.is_palindrome(word)