# Remove duplicate characters from a string.

def main():
    text = input("Enter text: ")
    seen = set()
    result_chars = []
    for ch in text:
        if ch not in seen:
            seen.add(ch)
            result_chars.append(ch)
    print(''.join(result_chars))


if __name__ == "__main__":
    main()
