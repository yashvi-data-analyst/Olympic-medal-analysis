# 📌 Olympic Medal Count by Country Project in Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
df = pd.read_csv("athlete_events.csv")
print("Dataset Loaded ✅")
print(df.head())

# Step 2: Filter Medal Winners Only
medals_df = df.dropna(subset=['Medal'])  # Keep only rows with medals

# Step 3: Group by Country and Medal Type
country_medals = medals_df.groupby(['NOC', 'Medal']).size().unstack().fillna(0)
country_medals['Total'] = country_medals.sum(axis=1)
top_countries = country_medals.sort_values('Total', ascending=False).head(30)

# Step 4: Plot Top 30 Countries by Medal Type
top_countries[['Gold', 'Silver', 'Bronze']].plot(kind='bar', stacked=True, figsize=(12,6), colormap='viridis')
plt.title("Top 30 Countries by Olympic Medals 🏅")
plt.xlabel("Country (NOC Code)")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.legend(title='Medal Type')
plt.tight_layout()
plt.show()

# Step 5: Year-wise Medal Trends for Top Country
usa_df = medals_df[medals_df['NOC'] == 'USA']
year_medals = usa_df.groupby('Year')['Medal'].count()

plt.figure(figsize=(10,5))
sns.lineplot(data=year_medals, marker="o", color="green")
plt.title("USA - Olympic Medal Count Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.grid(True)
plt.show()

# Step 6: Optional - Sport-wise Medal Distribution for India
india_df = medals_df[medals_df['NOC'] == 'IND']
india_sports = india_df['Sport'].value_counts().head(30)

plt.figure(figsize=(8,5))
sns.barplot(x=india_sports.values, y=india_sports.index, palette='magma')
plt.title("Top 30 Sports - India Medal Count")
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.show()

