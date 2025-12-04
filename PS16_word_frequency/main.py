# Word frequency counter from a paragraph (use dict).

def main():
    text = input("Enter a paragraph: ")
    words = [word.strip('.,!?;:"'').lower() for word in text.split()]
    freq = {}
    for word in words:
        if word:
            freq[word] = freq.get(word, 0) + 1
    print("Word frequencies:")
    for word, count in freq.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
