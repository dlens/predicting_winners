import pandas as pd
import matplotlib.pyplot as plt
import plotly as py
import tensorflow as tf
df = pd.read_excel('footballStats.xlsx')

x = df['PtsL']

plt.bar(df['Winner'], df['PtsW'])
plt.xlabel("Winning team")
plt.ylabel("Pts Scored")
plt.title("Pts Scored by winning team")
plt.show()

plt.bar(df['Week'], df['PtsW']-df['PtsL'])
plt.xlabel("Week")
plt.xticks(range(1,19))
plt.ylabel("Pts diff")
plt.title("random test")
plt.show()

