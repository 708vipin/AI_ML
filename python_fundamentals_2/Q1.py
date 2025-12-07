#Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on  these rules: 
# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%

salary = float(input("Enter the salary: "))
if salary < 30000:
    print(" tax_rate  = 5%")
elif 30000 <= salary <= 70000:       #range only works for integers
    print(" tax_rate = 15%")
else:
    print("tax_rate = 25%")        
