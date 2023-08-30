import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
# select top
# print(df.head(10))

# rows, columns count
# print(df.shape)

# list column name
# print(df.columns)

# check data is NaN
# print(df.isna())

# select last fows
# print(df.tail(10))

clean_df = df.dropna()
print(clean_df.tail())