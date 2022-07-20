"""
TASK 1
Write function calculate_freq(arr) to print frequency of elements without using collections.Counter()

input_data = ['hello', 'how', 'jack', 'day', 'how', 'night', 'hello', 'day', 'day']
result = calculate_freq(input_data)
print(result) --> {'day': 3, 'hello': 2, 'how': 2, 'jack': 1, 'night': 1}
"""


def calculate_freq(arr):
    freq = {}
    for word in arr:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] = freq[word] + 1
    return freq


print(calculate_freq(['hello', 'how', 'jack', 'day', 'how', 'night', 'hello', 'day', 'day']))

"""
TASK 2
Write function calculate_char_count(input_str) to print character count without using collections.Counter()

input_str = 'chihahua' 
result = calculate_char_count(input_str)
print(result) --> {'h': 3, 'a': 2, 'c': 1, 'i': 1, 'u': 1}
"""


def calculate_char_count(input_str):
    char_freq = {}
    for char in input_str:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] = char_freq[char] + 1
    return char_freq


print(calculate_char_count('chihahua'))

from collections import Counter
print(Counter('chihuahua'))
print(set('chihuahua'))