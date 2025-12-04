# Reverse a list using slicing.

def main():
    items = input("Enter list items separated by spaces: ").split()
    print(f"Reversed list: {items[::-1]}")


if __name__ == "__main__":
    main()
