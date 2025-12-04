# Remove a key-value pair from a dictionary.

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
    print(f"Original dictionary: {data}")
    key_to_remove = input("Enter key to remove: ")
    removed = data.pop(key_to_remove, None)
    if removed is None:
        print("Key not found.")
    else:
        print(f"Removed ({key_to_remove}: {removed})")
    print(f"Updated dictionary: {data}")


if __name__ == "__main__":
    main()
