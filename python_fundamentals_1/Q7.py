#Ask the user for a temperature in Celsius (string input). Convert it to float,then calculate and print temperature in Fahrenheit.
#Conversion FOrmula F = 9/5*C + 32

temp_c = float(input("Enter the temperature in Celsius: "))
temp_f = (9/5)*(temp_c) + 32
print("The temperature in Fahrenheit is,", temp_f)