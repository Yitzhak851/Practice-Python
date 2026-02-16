# Question 01:
# Question 1: Forbidden Characters
# Write a function in Python which gets as input arguments a sentence and a string of forbidden characters 
# and returns the sentence without the forbidden characters in it. 
# You may only use string manipulations (i.e. no function calls / libraries).
# Function signature should be:  def remove_forbidden_characters (sentence , forbidden_characters)
def remove_forbidden_characters(sentence, forbidden_characters):
    res = ""
    for ch in sentence:
        if ch not in forbidden_characters:
            res += ch
    return res

print(remove_forbidden_characters("Awesome sentence!", "aeos"))

# Question 2: Fun with Palindromes
# Part 1: Reverse a string
# Write a function that reverses a string (given as an input argument to the function) and returns the reversed string. 
# You may only use string slicing methods that you learned in class.
# Function signature should be: reverse(word).
def reverse(word):
    res = ""
    for i in range(len(word)-1, -1, -1):
        res += word[i]
    return res

print(reverse("Yitzhak Bar-or"))

# Part 2: Check if palindrome
# Write a function that determines if a given string is a palindrome (returns True/False).
# Function signature should be: is_palindrome(word).
# Part 3: Use previous parts
# Write a function that:
# 1.	Finds the largest palindrome which is a product of two 3-digit numbers (using functions from above as needed). Place the result in num1.
# 2.	Use string slicing to extract the palindrome's digits from even indices, and place the result in num2.
# Example: If num1 is: 12321, num2 should be: 131.
# You can use int() and str() to convert strings to integers and vice versa.
# Return the result as a tuple that contains the two integers: (num1, num2).
# Function signature should be: find_largest_palindrome().
def is_palindrome(word):
   # replace `pass` with your code
   pass
def find_largest_palindrome():
   # replace `pass` with your code
   pass

