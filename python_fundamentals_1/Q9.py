#Ask the user for: Principal(P), Rate(R), Time(T). Convert all to FLOAT and compute simple interest
#Formula is, S.I = (P*R*T)/100.....................

principal_P = float(input("Enter the Principal Amount: "))
rate_R = float(input("Enter the interest rate: "))
time_T = float(input("Enter the time in year: "))

simple_interest =(principal_P*rate_R*time_T)/100

print("The simple interest is,", simple_interest)