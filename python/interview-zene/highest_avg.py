# Q5. Find the highest Average score from below two-dimensional array.
def highest_avg(scores):
    # scores = [["Alex", "87"], ["bob", "100"], ["cindy", "64"], ["bob", "22"], ["cindy", "24"]]
    agg_scores = {}
    max_avg = None
    for user, score in scores:
        if user not in agg_scores:
            agg_scores[user] = (float(score), 1)
        else:
            score_sum, count = agg_scores[user]
            agg_scores[user] = (score_sum + float(score), count + 1)

    for user, (score_sum, count) in agg_scores.items():
        avg = score_sum / count
        if max_avg is None or avg > max_avg[1]:
            max_avg = (user, avg)

    return max_avg


input = [["Alex", 87], ["bob", 100], ["cindy", 64], ["bob", 22], ["cindy", 24]]
assert highest_avg(input) == ("Alex", 87.0)

import pandas as pd

df = pd.DataFrame(input)
print(df)
print('-------------------------')
max_index = df[1].idxmax()
print(input[max_index])
print('-------------------------')
mean_df = df.groupby(by=0).mean()
print(mean_df)
mean_max_idx = mean_df[1].idxmax()
print(mean_max_idx)

