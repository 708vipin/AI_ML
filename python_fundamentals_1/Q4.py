#The user enters a string containing a number(e.g.,).
#Convert it to
#•an integer 
#•a float 
#•a string again
#Print all three values with their types

user_str = input("Enter a string containing a number")
int_user_str = int(user_str)
float_user_str = float(user_str)

print(user_str, ",It's type is,", type(user_str))
print(int_user_str, ",It's type is,", type(int_user_str))
print(float_user_str, "It's type is,", type(float_user_str))