# Cognifyz Task 2 - Number Pattern

print("=" * 40)
print("       NUMBER PATTERN GENERATOR")
print("=" * 40)

rows = int(input("Enter the number of rows: "))

print("\nPattern:")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern generated successfully!")
