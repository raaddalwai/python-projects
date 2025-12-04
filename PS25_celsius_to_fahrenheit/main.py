# Take a temperature in Celsius and convert to Fahrenheit.

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} C = {fahrenheit} F")


if __name__ == "__main__":
    main()
