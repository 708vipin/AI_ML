#Ask the user for a string and check whether it is a palindrome or not?
#A Palindrome is a string that is same when read either from the forwards or from the backwards.

user_input = input("Enter the string: ")

reverse_input = user_input[::-1]

if user_input == reverse_input:
    print("Wow! It's a palindrome")
else:
    print("It's not a palindrome!")    