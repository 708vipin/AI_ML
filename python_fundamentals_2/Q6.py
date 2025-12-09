#Write a function to return the sum of digits of a number, n:

num = input("Enter the number: ")

digit_list = []

for digit in num:
    digit_list.append(int(digit))
print(sum(digit_list))