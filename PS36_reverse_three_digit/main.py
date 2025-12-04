# Input a three-digit number and print its reverse.

def main():
    num = int(input("Enter a three-digit number: "))
    n = abs(num)
    if n < 100 or n > 999:
        print("Number is not three digits.")
        return
    hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10
    reversed_num = ones * 100 + tens * 10 + hundreds
    if num < 0:
        reversed_num *= -1
    print(f"Reversed number: {reversed_num}")


if __name__ == "__main__":
    main()
