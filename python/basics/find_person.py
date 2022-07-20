"""
Write a method to find a name in a list and return it. The method needs to be case in-sensitive.
method name - find_person(list, text_to_find)
Examples:
    1 - find_person(['John', 'Smith'], 'john') should return 'John'
    2 - find_person(['stEVeN', 'Karol'], 'steven') should return 'stEVen'
    3 - find_person(['stEVeN', 'Karol'], 'StevEn') should return 'stEVen'
"""
def find_person(list, text_to_find):
    for person in list:
        if person.lower() in text_to_find.lower():
            return person


if __name__ == '__main__':
    print(find_person(['John', 'Smith'], 'john'))
    print(find_person(['stEVeN', 'Karol'], 'steven'))
    print(find_person(['stEVeN', 'Karol'], 'StevEn'))