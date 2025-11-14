# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # For each row, print asterisks side by side
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after a full row is printed
    print()
    
    row += 1
