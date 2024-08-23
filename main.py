# modules
import pandas as pd
import matplotlib.pyplot as plt

# global variables
quit = False

# dataframes
original_df = pd.read_csv('data/all_seasons.csv')
updated_df = original_df[['player_name', 'player_height', 'pts']]

# average height
avg_height = updated_df['player_height'].mean()
rounded_height = avg_height.round(1)

# average points
avg_points = updated_df['pts'].mean()
rounded_points = avg_points.round(1)

# sorted heights from shortest to tallest
sorted_df = updated_df.sort_values(by=['player_height'])

# defined functions
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(updated_df)

def showAvgHeight():
    print('Average Height of NBA Players:', rounded_height, 'cm')

def showAvgPoints():
    print('Average Points of NBA Players Per Game:', rounded_points, 'pts')

def showSortedData():
    print(sorted_df)

def showCharts():
    sorted_df.plot(
                 kind='line', 
                 x='player_height', 
                 y='pts', 
                 color='blue', 
                 alpha=0.3, 
                 title= 'Player Height vs Points Scored'
                )
    plt.show()

def userOptions():
    global quit
    
    print("""The long asked question, does height = performance? In this data analysis we are going to figure that out!!!
          Please select an option:
          1 - Show the original dataset
          2 - Show the updated Data Frame
          3 - Show the average height of NBA Players
          4 - Show the average points per game of NBA Players
          5 - Show data ordered from shortest to tallest
          6 - Visualise the comparison of height vs performance
          7 - Quit Program
          """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showAvgHeight()
        elif choice == 4:
            showAvgPoints()
        elif choice == 5:
            showSortedData()
        elif choice == 6:
            showCharts()
        elif choice == 7:
            quit = True
        else:
            print('A number between 1 and 7, come on!!!')

    except:
        print('Please enter a number!!!')

# main program
while not quit:
    userOptions()