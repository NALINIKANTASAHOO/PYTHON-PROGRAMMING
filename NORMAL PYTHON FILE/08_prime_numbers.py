# Concept: Prime Numbers
num = int(input("Enter a number to check if it's prime: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is Not a Prime number")
