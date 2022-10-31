# Q3. Return a function which accepts Array as input and returns Boolean value if sum of 2 number from array is equal
# to 11 - Explain the logic. What are the Max number of operations you are doing in this logic?


def two_sum(arr):
    seen = set()
    for j in arr:
        diff = 11 - j
        if diff in seen:
            return True
        else:
            seen.add(j)


assert two_sum([3, 9, 4, 7, 11, 0])
assert not two_sum([])
assert not two_sum([-20, 0, 54, 70, 10, 5, 2])
