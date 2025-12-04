# Merge two lists and sort them.

def read_numbers(prompt: str):
    raw = input(prompt)
    return [float(x) for x in raw.split()] if raw.strip() else []


def main():
    list1 = read_numbers("Enter first list of numbers: ")
    list2 = read_numbers("Enter second list of numbers: ")
    merged = sorted(list1 + list2)
    print(f"Merged and sorted list: {merged}")


if __name__ == "__main__":
    main()
