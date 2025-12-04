# Count occurrences of a specific character in a string.

def main():
    text = input("Enter text: ")
    target = input("Enter character to count: ")
    if not target:
        print("No character provided.")
        return
    char = target[0]
    count = sum(1 for c in text if c == char)
    print(f"'{char}' occurs {count} times.")


if __name__ == "__main__":
    main()
