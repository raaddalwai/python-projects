# Count how many digits are in a number (no string conversion).

def main():
    num = int(input("Enter an integer: "))
    n = abs(num)
    if n == 0:
        print("Number of digits: 1")
        return
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print(f"Number of digits: {count}")


if __name__ == "__main__":
    main()
