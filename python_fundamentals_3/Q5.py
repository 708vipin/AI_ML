#Create a dictionary where
#Keys = student names
#values = marks (Integers)
#Write a menu based program where user presses a key ("A","B","C","D") depending upon the operation they want to perform on the dictionary
# A - Add a student
# B - update marks
# C - search for a student
# D - Display all students and marks

stu_dict = {
    "Rahul": 90,
    "Vipin": 100
}

user_input = input("Enter either A, B, C, D: ")

if user_input == "A":
    print("Add")
elif user_input == "B":
    print("Update")
elif user_input == "C":
    print("Search")
elif user_input == "D":
    print("display all student")  
          