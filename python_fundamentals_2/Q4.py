#Write a function to return the count of digits in a number n,

num = input("Enter the number: ")

if "." in num:
    print(len(num)-1)
else:
    print(len(num))    
