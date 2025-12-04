# Print a right-angle star pattern.

def main():
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print("*" * i)


if __name__ == "__main__":
    main()
