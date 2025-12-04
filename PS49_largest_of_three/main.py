# Input three numbers; print the largest.

def main():
    nums = [float(input(f"Enter number {i + 1}: ")) for i in range(3)]
    print(f"Largest number: {max(nums)}")


if __name__ == "__main__":
    main()
