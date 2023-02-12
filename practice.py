

import pandas as pd

df = pd.read_csv(r"C:\NSEI.csv")

'''print(df)

print(df.columns)

print(df.loc[1226])'''

print(df.at[1226,"High"])
