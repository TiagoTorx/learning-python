show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # convert the string to all lower case
    temp = teststr.lower()

    # strip all the spaces and punctuation from the string
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c

    # now calculate the reverse of the string
    reversestr = ""
    strindx = len(newstr)-1
    while (strindx >= 0):
        reversestr += newstr[strindx]
        strindx -= 1

    if newstr == reversestr:
        return True
    return False

# This is how your code will be called.
# Your function should return whether a string is a palindrome.
# The code will count the number of correct answers
total = 0
test_words = ["Hello World!", "Radar", "Mama?", "Madam, I'm Adam.", "Race car!"]
for word in test_words:
    total += Answer.is_palindrome(word)