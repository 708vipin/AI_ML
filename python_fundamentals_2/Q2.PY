#Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

if a%2 == 0 and b%2 == 0:
    start = a
    end = b
    step = 2
    num = start
    while num <= end:
        print(num)
        num += step
elif a%2 == 0 and b%2 != 0:
    start = a
    end = b-1
    step = 2
    num = start
    while num <= end:
        print(num)
        num += step
elif a%2 != 0 and b%2 == 0:
    start = a+1
    end = b
    step = 2
    num = start
    while num <= end:
        print(num)
        num += step
elif a%2 != 0 and b%2 != 0:
    start = a+1
    end = b-1
    step = 2
    num = start
    while num <= end:
        print(num)
        num += step
