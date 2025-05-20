# Author: 2025 Mikhail Ibrahim
# Date: May 19th, 2025
# Description: A crash-proof Python program that calculates the middle percentage
# mark based on the Ontario grading levels (e.g., 4+, 3-, etc.). It handles invalid
# input gracefully and ensures only valid level strings return corresponding marks.


def calc_mark(level):
    """
    Returns the middle percentage mark for a given Ontario grade level.
    If input is invalid, returns -1.
    """
    if level == "4+":
        mark = 95
    elif level == "4":
        mark = 87
    elif level == "4-":
        mark = 83
    elif level == "3+":
        mark = 78
    elif level == "3":
        mark = 75
    elif level == "3-":
        mark = 72
    elif level == "2+":
        mark = 68
    elif level == "2":
        mark = 65
    elif level == "2-":
        mark = 62
    elif level == "1+":
        mark = 58
    elif level == "1":
        mark = 55
    elif level == "1-":
        mark = 52
    elif level == "R":
        mark = 30
    else:
        mark = -1
    return mark


def main():
    print("Welcome to the Ontario Grade Level to Mark Converter")

    level = input("Enter your grade level (e.g., 4+, 3-, 2): ").strip()

    result = calc_mark(level)

    if result == -1:
        print("Invalid Response. Please enter a valid grade level such as 4+, 3, or R.")
    else:
        print(f"The middle percentage mark for level '{level}' is: {result}%")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
