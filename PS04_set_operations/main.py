# Input two sets and print union, intersection, and difference.

def read_set(prompt: str):
    raw = input(prompt)
    return set(item.strip() for item in raw.split() if item.strip())


def main():
    set_a = read_set("Enter elements of set A separated by spaces: ")
    set_b = read_set("Enter elements of set B separated by spaces: ")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"A - B difference: {set_a - set_b}")
    print(f"B - A difference: {set_b - set_a}")


if __name__ == "__main__":
    main()
