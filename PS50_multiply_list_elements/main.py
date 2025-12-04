# Multiply all elements of a list.

def main():
    numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
    product = 1
    for num in numbers:
        product *= num
    print(f"Product of elements: {product}")


if __name__ == "__main__":
    main()
