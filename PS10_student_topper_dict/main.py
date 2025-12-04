# Create a dictionary of 5 students marks and print topper.

def main():
    marks = {}
    for i in range(5):
        name = input(f"Enter name for student {i + 1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    topper = max(marks, key=marks.get)
    print(f"Topper: {topper} with {marks[topper]} marks")


if __name__ == "__main__":
    main()
