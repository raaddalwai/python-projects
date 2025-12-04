# Find factorial of a number using a loop.

def main():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")


if __name__ == "__main__":
    main()
