# Find common values between two dictionaries.

def parse_dict(raw: str):
    result = {}
    for pair in raw.split():
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key] = value
    return result


def main():
    dict_a = parse_dict(input("Enter key:value pairs for dict A: "))
    dict_b = parse_dict(input("Enter key:value pairs for dict B: "))
    common_values = set(dict_a.values()) & set(dict_b.values())
    print(f"Dictionary A: {dict_a}")
    print(f"Dictionary B: {dict_b}")
    print(f"Common values: {common_values}")


if __name__ == "__main__":
    main()
