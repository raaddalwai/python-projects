# Input marks of 5 subjects; print total, average, and percentage.

def main():
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    total = sum(marks)
    average = total / 5
    percentage = (total / (5 * 100)) * 100
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    main()
