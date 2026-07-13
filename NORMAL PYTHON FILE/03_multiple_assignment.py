# Concept: Multiple Assignment
print("Enter three numbers separated by spaces:")
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

print("a =", a, ", b =", b, ", c =", c)

# Swapping using multiple assignment
a, b = b, a
print("After swapping a and b:")
print("a =", a, ", b =", b)
