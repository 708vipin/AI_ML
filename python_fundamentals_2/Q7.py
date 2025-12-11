#Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.
while True:
    user_input = input("Please provide your input: ")

    if user_input != "Quit":
        num = float(user_input)
        if num > 0:
         print("Positive")
        elif num < 0:
         print("Negative")
        else:
         print("Zero")
    else:
      break     
    

    

    


