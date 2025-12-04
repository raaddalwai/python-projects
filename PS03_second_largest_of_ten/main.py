# Input 10 numbers into a list and print the second largest.

def main():
    numbers = []
    for idx in range(10):
        value = float(input(f"Enter number {idx + 1}: "))
        numbers.append(value)
    unique_sorted = sorted(set(numbers))
    if len(unique_sorted) < 2:
        print("Second largest does not exist (not enough unique numbers).")
    else:
        print(f"Second largest: {unique_sorted[-2]}")


if __name__ == "__main__":
    main()
