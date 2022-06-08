'''
Given a map of team scores, find average of scores starting with a given letter.
Implement find_avg(score_map, start_letter) and return average

Example:
    {
        "Arizona": 10,
        "California": 12,
        "Alabama": 20,
        "arkansas": 3
    }

find_avg(score_map, 'a') should return 11
find_avg(score_map, 'c') should return 12
find_avg(score_map, 'k') should return 0
'''


def find_avg(score_map, start_letter):
    Sum = 0
    count = 0
    for key, value in score_map.items():
        first_letter = key[0]
        if first_letter.lower() == start_letter:
            Sum += value
            count = count +1
    if count == 0:
        return 0.0
    average_score = Sum / count
    return average_score



if __name__ == '__main__':
    scrmap = {
        "Arizona": 10,
        "California": 12,
        "Alabama": 20,
        "arkansas": 3
    }
    print(find_avg(scrmap, 'a'))
    print(find_avg(scrmap, 'c'))
    print(find_avg(scrmap, 'k'))

    other_scr_map = {
        "Arizona": 22,
        "arkansas": -22
    }
    print(find_avg(other_scr_map, 'a'))