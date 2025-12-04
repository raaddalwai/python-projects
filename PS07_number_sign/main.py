# Input a number and check if it is positive, negative, or zero.

def main():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    main()
