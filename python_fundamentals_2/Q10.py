#Let's create a "Number guessing game". Given a secret number (already decided by you), write a program that asks the user to guess it & print.
#"Too High" if the guess is above the number
#"Too low" if the guess is below
#"Correct!" if the guess matches


sec_num = 75
while True:
    user_input = float(input("Enter your guess: "))
    if user_input > sec_num:
        print("Too High")
    elif user_input < sec_num:
        print("Too low")
    else:
        print("Correct!")
        break        

