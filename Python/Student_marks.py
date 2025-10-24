import pandas as pd
import numpy as np

data = {
    "Name": ["Akhil", "Ravi", "Teja", "Kiran", "Sai"],
    "Maths": [78, 85, 92, 68, 80],
    "Science": [88, 79, 95, 74, 82],
    "English": [90, 70, 89, 75, 85]
}

df = pd.DataFrame(data)

print("===== Student Marks Data =====")
print(df)

averages = np.mean(df[["Maths", "Science", "English"]], axis=1)
df["Average"] = averages

highest = np.max(df[["Maths", "Science", "English"]].values)
lowest = np.min(df[["Maths", "Science", "English"]].values)

print("\n===== Updated Data with Averages =====")
print(df)

print("\n===== Summary =====")
print(f"Highest mark in the class: {highest}")
print(f"Lowest mark in the class: {lowest}")
