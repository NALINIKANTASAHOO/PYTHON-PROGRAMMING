# Concept: Fibonacci Logic
n = int(input("Enter number of Fibonacci terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
