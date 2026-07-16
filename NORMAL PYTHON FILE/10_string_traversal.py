# Concept: String Traversal
text = input("Enter a string: ")

print("Traversing the string character by character:")
for ch in text:
    print(ch)

vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels in the string:", count)
