# Given a tuple of numbers, print all numbers greater than 50.

def main():
    numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())
    greater = [n for n in numbers if n > 50]
    print(f"Numbers greater than 50: {greater}")


if __name__ == "__main__":
    main()
