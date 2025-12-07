#Take a decimal number (say 45.78) and output it integer and decimal parts like this, integer: 45, decimal:78;

num = float(input("Enter the number: "))

integer_part = int(num)
decimal_part = num - integer_part

print("The integer part of the given number is: ", integer_part)
print("The decimal part of the given number is: ", decimal_part)
