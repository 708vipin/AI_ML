# Input two lists of integers from the user. Merge them into one list and sort the result

list_1 = input("Enter the first list: ")
list_2 = input("Entrer the second list: ")


list_1 = [int(x.strip()) for x in list_1.split(",")]
list_2 = [int(x.strip()) for x in list_2.split(",")]

merged_list = list_1 + list_2

merged_list.sort()
print(merged_list)