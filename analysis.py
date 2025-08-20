import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataframe = pd.read_csv("Zomato-data-.csv")
print("Columns available:", dataframe.columns)   # ✅ helps check exact names
print(dataframe.head())

# Clean 'rate' column
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    try:
        return float(value)
    except:
        return np.nan   # handle cases like "NEW" or "nan"

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())
dataframe.info()

# -----------------------------
# Type of Restaurant
plt.figure(figsize=(8,5))
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of Restaurant")
plt.xticks(rotation=45)
plt.title("Count of Restaurant Types")
plt.show()

# -----------------------------
# Votes by Restaurant Type
grouped = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped})
plt.figure(figsize=(8,5))
plt.plot(result.index, result['votes'], c="blue", marker="o")
plt.xlabel("Type of Restaurant", c="red", size=12)
plt.ylabel("Votes", c="red", size=12)
plt.title("Votes by Restaurant Type")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Ratings Distribution
plt.figure(figsize=(8,5))
plt.hist(dataframe['rate'], bins=5, color="skyblue", edgecolor="black")
plt.title("Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
data = dataframe['approx_cost(for two people)']   # ✅ fixed column name
sns.countplot(x=data)
plt.title("Approx Cost for 2 People")
plt.show()

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=dataframe)
plt.title("Online Order vs Ratings")
plt.show()

pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order',  aggfunc='size', fill_value=0)

plt.figure(figsize=(8,6))
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap of Restaurant Type vs Online Order")
plt.xlabel("Online Order")
plt.ylabel("Restaurant Type")
plt.show()
