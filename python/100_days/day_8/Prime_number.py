# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0 :
            is_prime = False
    if number < 1:
        print("it is a negative number")
    elif is_prime:
        print("the number is prime")
    else:
        print("the number is not prime")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

