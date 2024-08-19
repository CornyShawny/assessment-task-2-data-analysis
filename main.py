import pandas as pd
import matplotlib.pyplot as plt

all_seasons = pd.read_csv('data/all_seasons.csv')
all_seasons = all_seasons[['player_name', 'player_height', 'pts']]
avg_height = all_seasons['player_height'].mean()
avg_pts = all_seasons['pts'].mean()

all_seasons = all_seasons.sort_values(by=['player_height'])
print(all_seasons)

all_seasons.plot(
                 kind='bar', 
                 x='player_height',
                 y='pts',
                 color='blue',
                 alpha=1,
                 title= 'Player Height = Points Scored?'
                )
plt.show()