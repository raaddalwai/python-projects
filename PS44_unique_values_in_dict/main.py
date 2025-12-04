# Count how many unique values exist across dictionary items.

def parse_dict(raw: str):
    result = {}
    for pair in raw.split():
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key] = value
    return result


def main():
    data = parse_dict(input("Enter key:value pairs separated by spaces: "))
    unique_values = set(data.values())
    print(f"Dictionary: {data}")
    print(f"Unique values count: {len(unique_values)}")


if __name__ == "__main__":
    main()
