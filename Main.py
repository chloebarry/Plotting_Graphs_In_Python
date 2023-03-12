

import numpy as np
# import matplotlib.pyplot as plt
# import numpy as np

import pandas as pd

from matplotlib import pyplot as plt

# importing the csv file
df = pd.read_csv("Votes.csv")
print(df)

# Initialise a figure. subplots() with no args gives one plot.
fig, ax = plt.subplots()

# data preparation
years = df['year']
x = np.arange(len(years))

# setting the width value
width = 0.15

# Plotting the bars
ax.bar(x - 3 * width / 2, df['conservative'], width, label='Conservative', color='#0343df')
ax.bar(x - width / 2, df['labour'], width, label='Labour', color='#e50000')
ax.bar(x + width / 2, df['liberal'], width, label='Liberal', color='#ffff14')
ax.bar(x + 3 * width / 2, df['others'], width, label='Others', color='#929591')

# Customising some display properties
ax.set_ylabel('Seats')
ax.set_title('UK election results')
ax.set_xticks(x)  # This ensures we have one tick per year, otherwise we get fewer
ax.set_xticklabels(years.astype(str).values, rotation='vertical')
ax.legend()

# adding the plotted line and the grid pattern
ax.plot(x, df['conservative'] - df['labour'], label='Conservative lead over Labour', color='black', linestyle='dashed')
ax.grid(color='#eeeeee')
ax.set_axisbelow(True)
ax.set_ylim([-500, 500])

# Showing the graph
plt.show()
