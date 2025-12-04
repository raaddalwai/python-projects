# Reverse a dictionary (swap keys & values).

def parse_dict(raw: str):
    result = {}
    for pair in raw.split():
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key] = value
    return result


def main():
    raw = input("Enter key:value pairs separated by spaces: ")
    data = parse_dict(raw)
    reversed_dict = {value: key for key, value in data.items()}
    print(f"Original: {data}")
    print(f"Reversed: {reversed_dict}")


if __name__ == "__main__":
    main()
