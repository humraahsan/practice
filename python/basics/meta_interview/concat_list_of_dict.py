# Write a Python script to concatenate a list of dictionaries to create a new dictionary.
# Sample list:
alist = [{1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 3: 60}]
diction = {1: 10, 2: 20, 3: 90, 4: 40, 5: 50}


def remove_duplicates(alist):
    result = {}
    for d in diction:
        for k, v in alist:
            if k in result:
                result[k] += v
            else:
                result[k] = v


