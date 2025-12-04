# Find the longest word in a sentence.

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    if not words:
        print("No words provided.")
        return
    longest = max(words, key=len)
    print(f"Longest word: {longest}")


if __name__ == "__main__":
    main()
