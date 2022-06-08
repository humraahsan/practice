"""
Find min and max values from a given array and print them
min_max(integer_values)

min_max([3,5,21,2]) should print 2, 21
min_max([3,5]) should print 3, 5
min_max([9, 9]) should print 9, 9
min_max([11]) should print 11, 11

ii

Find average of list excluding minimum and maximum number.
min_max_avg([3,5,21,2]) should return 4
min_max_avg([3,5]) should return 0
min_max_avg([8, 12, 10, 4, 6, 14]) should return 9
"""

def min_max(numbers):
    first_no = numbers[0]
    min = first_no
    max = first_no
    for number in numbers:
        if min >= number:
            min = number
        if max <= number:
            max = number
    return min, max

def min_max_avg(numbers):
    no_sum = 0
    count = len(numbers) -2
    first_no = numbers[0]
    min = first_no
    max = first_no
    for number in numbers:
        if min >= number:
            min = number
        if max <= number:
            max = number
        no_sum += number

    if count <= 0:
        return 0.0
    min_max_sum = no_sum - (min + max)
    average = min_max_sum / count
    return average





if __name__ == '__main__':
    print(min_max([3, 5, 21, 2]))
    print(min_max([3, 5]))
    print(min_max([9, 9]))
    print(min_max([11]))

    print(min_max_avg([3, 5, 21, 2]))
    print(min_max_avg([3, 5]))
    print(min_max_avg([8, 12, 10, 4, 6, 14]))
