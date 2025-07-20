# pattern_drawing.py

# Prompt the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))

    if size > 0:
        row = 0
        while row < size:
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    else:
        print("Please enter a positive integer.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
