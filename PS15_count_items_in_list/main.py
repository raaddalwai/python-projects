# Count how many times each item appears in a list.

def main():
    items = input("Enter list items separated by spaces: ").split()
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    print("Item counts:")
    for key, value in counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
