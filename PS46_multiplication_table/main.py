# Input a number; print multiplication table (1–10).

def main():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    main()
