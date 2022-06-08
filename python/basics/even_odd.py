"""
write a method that takes two numbers as input and returns all odd numbers between them
get_odd_between(low, high)
- returns list of odd numbers between these numbers
"""


def get_odd_between(low, high):
    result = []
    for i in range(low, high):
        if i % 2 == 1:
            result.append(i)
    return result

if __name__ == '__main__':
    print(get_odd_between(10, 34))