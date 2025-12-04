# Convert two lists (keys, values) into a dictionary.

def main():
    keys = input("Enter keys separated by spaces: ").split()
    values = input("Enter values separated by spaces: ").split()
    length = min(len(keys), len(values))
    dictionary = {keys[i]: values[i] for i in range(length)}
    print(f"Dictionary: {dictionary}")


if __name__ == "__main__":
    main()
