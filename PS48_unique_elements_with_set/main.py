# Input a list and print all unique elements using a set.

def main():
    items = input("Enter list items separated by spaces: ").split()
    unique_items = set(items)
    print(f"Unique elements: {unique_items}")


if __name__ == "__main__":
    main()
