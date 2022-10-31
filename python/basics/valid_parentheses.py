def valid_pair(input_str):
    pairs = {")": "(", "}": "{", "]": "["}
    seen = []
    for char in input_str:
        if char in pairs:
            if not seen:
                return False
            elif seen.pop() == pairs[char]:
                return True
            else:
                return False
        else:
            seen.append(char)
    if len(seen) > 0:
        return False


print(valid_pair("({[]})"))
