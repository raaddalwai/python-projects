# Sum of digits of a number using a loop.

def main():
    num = int(input("Enter an integer: "))
    total = 0
    n = abs(num)
    while n > 0:
        total += n % 10
        n //= 10
    print(f"Sum of digits: {total}")


if __name__ == "__main__":
    main()
