# Find the index of a value in a tuple (handle value not present).

def main():
    items = tuple(input("Enter tuple items separated by spaces: ").split())
    value = input("Enter value to find: ")
    try:
        idx = items.index(value)
        print(f"Index of {value}: {idx}")
    except ValueError:
        print(f"{value} not found in tuple")


if __name__ == "__main__":
    main()
