# Concept: if-else
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print(num, "is Zero")
