# Input a string and count vowels, consonants, digits, and spaces.

def main():
    text = input("Enter text: ")
    vowels_set = set("aeiouAEIOU")
    vowels = sum(1 for ch in text if ch in vowels_set)
    digits = sum(1 for ch in text if ch.isdigit())
    spaces = text.count(" ")
    consonants = sum(1 for ch in text if ch.isalpha() and ch not in vowels_set)
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")


if __name__ == "__main__":
    main()
