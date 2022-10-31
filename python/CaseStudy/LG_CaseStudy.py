# importing packages
import pandas as pd
import numpy as np
df = pd.read_csv(r'/Users/humraahsan/devbox/practice/python/CaseStudy/Case Study Dataset.csv', skip_blank_lines=True)
df = df.dropna(how='all')
#print(df)
df["LeadQuality"] = " "
for i, row in df.iterrows():
    print("=========END OF ROW++++++++++++")
    if pd.isnull(row["CallStatus"]):
        df.at[i, "LeadQuality"] = "Unknown"
    elif 'Closed' in row["CallStatus"]:
        df.at[i, "LeadQuality"] = "Closed"
    elif "EP" in row["CallStatus"]:
        df.at[i, "LeadQuality"] = "Good Lead"
    elif 'contact' or "Contacted" in row['CallStatus']:
        df.at[i, "LeadQuality"] = "Bad Lead"
    print(df.at[i, 'CallStatus'], df.at[i, 'LeadQuality'])

print(df["LeadQuality"].unique())
print(df["CallStatus"].unique())


df.to_csv('my_data.csv')




