import pandas as pd
import numpy as np


df = pd.read_csv("test1.csv")


columns = df.columns
print("Columns in dataset:", columns)

#Identify numeric columns automatically (subjects)
numeric_cols = df.select_dtypes(include='number').columns

#Replace invalid values (optional: 0 treated as missing)
df[numeric_cols] = df[numeric_cols].replace(0, np.nan)

#Fill missing values with column mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

#Handle text column (name)
df["Name"] = df["Name"].fillna("Unknown")

#Final cleaned data
print("\nCleaned Data:")
print(df)

#Save cleaned file
df.to_csv("cleaned_students.csv", index=False)