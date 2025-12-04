# Convert a list to tuple and tuple back to list.

def main():
    items = input("Enter list items separated by spaces: ").split()
    as_tuple = tuple(items)
    back_to_list = list(as_tuple)
    print(f"Tuple: {as_tuple}")
    print(f"List again: {back_to_list}")


if __name__ == "__main__":
    main()
