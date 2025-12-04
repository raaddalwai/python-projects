# Input a sentence and print each word on a new line.

def main():
    sentence = input("Enter a sentence: ")
    for word in sentence.split():
        print(word)


if __name__ == "__main__":
    main()
