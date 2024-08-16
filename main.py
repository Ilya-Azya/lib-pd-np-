import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
url = "owid-covid-data.csv"
df = pd.read_csv(url)

# Clear
df = df[df['location'] == 'World']
df['date'] = pd.to_datetime(df['date'])
df = df[['date', 'new_cases', 'new_deaths']]

df.fillna(0, inplace=True)


df['rolling_avg_cases'] = df['new_cases'].rolling(window=7).mean()
df['rolling_avg_deaths'] = df['new_deaths'].rolling(window=7).mean()

# visual
plt.figure(figsize=(14, 7))
plt.plot(df['date'], df['rolling_avg_cases'], label='New Cases (7-day avg)')
plt.plot(df['date'], df['rolling_avg_deaths'], label='New Deaths (7-day avg)')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('COVID-19 Global Cases and Deaths')
plt.legend()
plt.show()
