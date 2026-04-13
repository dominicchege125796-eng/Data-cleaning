import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("messy_students.csv")
#drop dulicates based on "admission" column, keeping the first occurrence
df = df.drop_duplicates(subset=["admission"], keep="first")

#drop duplicates based on "name" column, keeping the first occurrence
df = df.drop_duplicates(subset=["name"], keep="first")


df["math"] = df["math"].replace(0, np.nan)
df["math"] = df["math"].fillna(df["math"].mean())

df["english"] = df["english"].replace(0, np.nan)
df["english"] = df["english"].fillna(df["english"].mean())

df["science"] = df["science"].replace(0, np.nan)
df["science"] = df["science"].fillna(df["science"].mean())

df["math"] = df["math"].apply(lambda x: x if 0 <= x <= 100 else np.nan)
df["science"] = df["science"].apply(lambda x: x if 0 <= x <= 100 else np.nan)

df["math"] = df["math"].fillna(df["math"].mean())
df["science"] = df["science"].fillna(df["science"].mean())
df["name"] = df["name"].str.strip().str.title()
df = df.dropna(subset=["name"])
df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["date"] = df["date"].fillna(df["date"].mode()[0])
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

#calculations
def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["average"] = df[["math", "english", "science"]].mean(axis=1)
df["grade"] = df["average"].apply(grade)
df.to_csv("cleaned_students.csv", index=False)

#graph representation
plt.figure(figsize=(10, 6))
plt.hist(df["average"], bins=10, edgecolor="black")
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.75)

plt.savefig("average_score_distribution.png")
plt.plot()

print("Class Average:", df["average"].mean())
print("Highest Score:", df["average"].max())
print("Lowest Score:", df["average"].min())

top_students = df.sort_values("average", ascending=False).head(3)
print(top_students[["name", "admission", "average"]])

at_risk = df[df["average"] < 50]
print(at_risk[["name", "average"]])

print("Math avg:", df["math"].mean())
print("English avg:", df["english"].mean())
print("Science avg:", df["science"].mean())
