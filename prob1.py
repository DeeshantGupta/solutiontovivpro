# Solution of 1.1 Data Processing.

import pandas as pd

#Data reading
df = pd.read_json('playlist[76][36][48][6].json', orient='columns')
df.reset_index(inplace=True)

#Saving to a csv file
df.to_csv('output.csv', index=False)

