# Input age; check if eligible for voting.

def main():
    age = int(input("Enter age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")


if __name__ == "__main__":
    main()
