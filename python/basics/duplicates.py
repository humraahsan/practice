# Find duplicate characters in a string
def duplicate(input_str):
    seen = {}
    result = set()
    for char in input_str:
        if char not in seen:
            seen[char] = 1
        else:
            if seen[char] == 1:
                result.add(char)
                seen[char] += 1
    return result


print(duplicate("abracaddab"))


def dup(original_str):
    seen = {}
    result = []
    for char in original_str:
        if char not in seen:
            seen[char] = 1
        else:
            result.append(char)
            seen[char] += 1
    return result

print(dup('aaaa'))
