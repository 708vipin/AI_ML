#Ask the user for a string and check whether it is a palindrome or not?
#A Palindrome is a string that is same when read either from the forwards or from the backwards.

user_input = input("Enter the string: ")

a = len(user_input)

if a%2 == 0:
    b = a/2