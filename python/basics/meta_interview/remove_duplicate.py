# Remove duplicates from a list
# Sample list:
alist = [3, 2, 2, 1, 1, 1]


def remove_dup(alist):
    seen = []
    for element in alist:
        if element not in seen:
            seen.append(element)
    return seen


def remove_duplicates(alist):
    seen = {}
    return set(alist)


print(remove_duplicates(alist))

print(remove_dup(alist))
