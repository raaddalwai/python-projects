# Remove duplicates from a list without using set().

def main():
    items = input("Enter list items separated by spaces: ").split()
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    print(f"List without duplicates: {unique}")


if __name__ == "__main__":
    main()
