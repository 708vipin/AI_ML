#Write a function is_prime() that returns True if n is a prime number and False otherwise, using a loop.
def is_prime():
    num = int(input("Enter the number: "))

    for n in range(2, num-1):
        if num%n == 0:
            print("False, the number is not Prime")
            break
    else:
        print("True, the number is prime") 
            

is_prime()            
     