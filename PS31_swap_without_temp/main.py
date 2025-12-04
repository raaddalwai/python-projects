# Swap two variables without using a third variable.

def main():
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    a, b = b, a
    print(f"After swap -> first: {a}, second: {b}")


if __name__ == "__main__":
    main()
