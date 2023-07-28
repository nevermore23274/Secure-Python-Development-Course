"""
 Helpful links:
 https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#histograms
 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
"""
# Import(s)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv's, store in numpy arrays and pandas dataframe
housing = pd.read_csv('Housing.csv')
housing_data = np.array(housing)
population = pd.read_csv('PopChange.csv')
pop_data = np.array(population)
# Menu lines for neatness
MENU_LINE = '*'*10
EXIT_LINE = '*'*41


def pop_calc(pop_num):
    """
    Calculate stats for population change columns
    """
    # Set baseline values
    pop_num = int(pop_num)
    pop_count = 0
    pop_mean_value = 0
    pop_min_value = 0
    pop_max_value = 0
    pop_standard_dev = 0

    print("\n" + "The Statistics For This Column Are: ")
   # Use .iloc to get stats column indexed at value
   # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
    pop_mean_value = round(population.iloc[:,pop_num].mean(), 1)
    pop_standard_dev = round(population.iloc[:,pop_num].std(), 1)
    pop_max_value = round(population.iloc[:,pop_num].max(), 1)
    pop_min_value = round(population.iloc[:,pop_num].min(), 1)
    pop_count = len(population.iloc[:,pop_num])
    # Use str() to avoid TypeError
    print("Count = " + str(pop_count))
    print("Mean = " + str(pop_mean_value))
    print("Standard deviation = ", str(pop_standard_dev))
    print("Min = " + str(pop_min_value))
    print("Max = " + str(pop_max_value))
    print("The histogram of this column is now displayed.")
    # Set density to true based on:
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    # Leave 55 to see smaller data bars (one on far right)
    plt.hist(pop_data[:,pop_num], 55, density=True)
    plt.grid(True)
    plt.show()


def housing_calc(house_num):
    """
    Analyze housing data, get column stats
    """
    # Set baseline values
    house_num = int(house_num)
    house_count = 0
    house_mean_value = 0
    house_min_value = float(housing_data[house_count][house_num])
    house_max_value = float(housing_data[house_count][house_num])
    house_standard_dev = 0

    print("\n" + "The Statistics For This Column Are: ")
    # Use .iloc to get stats column indexed at value
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
    house_mean_value = round(housing.iloc[:,house_num].mean(), 1)
    house_count = round(len(housing.iloc[:,house_num]), 1)
    house_min_value = round(housing.iloc[:,house_num].min(), 1)
    house_max_value = round(housing.iloc[:,house_num].max(), 1)
    house_standard_dev = round(housing.iloc[:,house_num].std(), 1)
    # Use str() to avoid TypeError
    print("Count = " + str(house_count))
    print("Mean = " + str(house_mean_value))
    print("Standard Deviation = " + str(house_standard_dev))
    print("Min = " + str(house_min_value))
    print("Max = " + str(house_max_value))
    print("The histogram of this column is now displayed.")
    # Set density to true based on:
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    plt.hist(pop_data[:,house_num], density=True)
    plt.grid(True)
    plt.show()

def get_pop():
    """
    Prompt user for column name in population change csv, display histogram
    """
    # First 3 cols seem irrelevant for assignment
    while True:
        print("\n" + "You Have Entered Population Data.")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        user_pop_input = input("\n" + "> ")

        if user_pop_input in ('A', 'a'):
            pop_calc(4) # 5th column

        elif user_pop_input in ('B', 'b'):
            pop_calc(5) # 6th column

        elif user_pop_input in ('C', 'c'):
            pop_calc(6) # 7th column

        elif user_pop_input in ('D', 'd'):
            print("\n" + EXIT_LINE + "\nYou selected to exit the population menu.\n" + EXIT_LINE)
            break


def get_housing():
    """
    Prompt user: Input column for analysis, display the histogram
    """
    while True:
        # Cols 3 (NUNITS) and 5 (Weight) seem irrelevant for assignment
        print("\n" + "You Have Entered Housing Data.")
        print("\n" + "Select The Column You Want to Analyze:")
        print("a. Age")
        print("b. Bedroom")
        print("c. Built Year")
        print("d. Rooms")
        print("e. Utility")
        print("f. Exit Columns")
        user_house_input = input("\n" + "> ")

        if user_house_input in ('A', 'a'):
            housing_calc(0) # 1st column

        elif user_house_input in ('B', 'b'):
            housing_calc(1) # 2nd column

        elif user_house_input in ('C', 'c'):
            housing_calc(2) # 3rd column

        elif user_house_input in ('D', 'd'):
            housing_calc(4) # 4th column

        elif user_house_input in ('E', 'e'):
            housing_calc(6) # 7th column

        elif user_house_input in ('F', 'f'):
            print(EXIT_LINE + "\nYou selected to exit the housing menu.\n" + EXIT_LINE)
            break

# Main program display and functionality
print(MENU_LINE + " Welcome to the Python Data Analysis App " + MENU_LINE)
while True:
    print("\n" + "Select the file you want to analyze:")
    print("1. Population Data ")
    print("2. Housing Data ")
    print("3. Exit The Program ")

    # Error and input handling for menu
    try:
        user_input = int(input("\n" + "> "))
    except ValueError:
        print("Invalid input. Pick number 1, 2, or 3: ")
    if user_input == 1:
        get_pop()
    elif user_input == 2:
        get_housing()
    elif user_input == 3:
        print("\n" + MENU_LINE + " Thanks for using the Data Analysis App " + MENU_LINE)
        break
    else:
        print("Invalid input. Pick number 1, 2, or 3.")
