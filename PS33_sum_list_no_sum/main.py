# Find the sum of all elements in a list without using sum().

def main():
    numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
    total = 0
    for num in numbers:
        total += num
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
