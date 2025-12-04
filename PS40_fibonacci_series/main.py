# Print Fibonacci series up to n terms.

def main():
    n = int(input("Enter number of terms: "))
    if n <= 0:
        print("Number of terms must be positive.")
        return
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(sequence)


if __name__ == "__main__":
    main()
