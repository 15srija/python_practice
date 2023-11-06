number=int(input("Enter a number:"))


def prime_checker(n):
    is_prime=True
    if n==1:
        print("It is not a prime number")
    for i in range(2,round(n/2)):
        if n%i==0:
            is_prime=False
    if is_prime==False:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is prime number")

prime_checker(n=number)