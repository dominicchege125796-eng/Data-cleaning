import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv("messy_students.csv")

#view duplicates
df = data.duplicated(subset="admission" ).sum()

#drop duplicates by admission number
data = data.drop_duplicates(subset="admission")

#drop by name
data = data.drop_duplicates(subset="name")

#replacing null values in math column with mean
data["math"] = data["math"].replace(0, np.nan)
data["math"] = data["math"].fillna(data["math"].mean())

#replacing null values in english column with mean
data["english"] = data["english"].replace(0, np.nan)
data["english"] = data["english"].fillna(data["english"].mean())

#replacing null values in science column with mean
data["science"] = data["science"].replace(0, np.nan)
data["science"] = data["science"].fillna(data["science"].mean())

#values less than 0 or exceed the average limit
data["math"] = data["math"].apply(lambda x: x if 0 <= x <= 100 else np.nan)
data["science"] = data["science"].apply(lambda x: x if 0 <= x <= 100 else np.nan)

data["math"] = data["math"].fillna(data["math"].mean())
data["science"] = data["science"].fillna(data["science"].mean())

#missing names
data["name"] = data["name"].fillna("Unknown")
data["name"] = data["name"].str.strip().str.title()

#drop columns with missing name
data = data.dropna(subset=["name"])

#fixing dates
# Convert to datetime
data["date"] = pd.to_datetime(data["date"], errors="coerce")

# Fill missing dates
data["date"] = data["date"].fillna(data["date"].mode()[0])

# Standardize format
data["date"] = data["date"].dt.strftime("%Y-%m-%d")

data.to_csv("cleaned.csv", index=False)
print(data)
