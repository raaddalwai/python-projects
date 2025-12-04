# Check if a given string is a palindrome.

def main():
    text = input("Enter text: ")
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    if cleaned == cleaned[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
