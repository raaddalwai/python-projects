# Print characters at even index positions.

def main():
    text = input("Enter text: ")
    result = ''.join(ch for idx, ch in enumerate(text) if idx % 2 == 0)
    print(f"Characters at even indices: {result}")


if __name__ == "__main__":
    main()
