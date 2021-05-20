import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Hey there! which city would you like to analyze\n Choose from the following cities\n 1.Chicago 2.New york city 3.Washington")
        city = input ("\nEnter the number of the city of your choice from the cities listed above, 1, 2 or 3 without space or periods: ")
        if city == '1':
            city = 'chicago'
            break
        elif city == '2':
            city = 'new york city'
            break
        elif city == '3':
            city = 'washington'
            break
        else:
            print('Kindly enter the number of the city you want only\n You have option 1, 2 or 3\n No spaces or periods please')

    print("\nYou have chosen to analyze data for {}".format(city.title()))
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = { 'january': 1, 'february': 2, 'march': 3,
              'april': 4, 'may': 5, 'june': 6, 'all': 7 }
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nWhich month would you like to analyze")
        print("\nType in any month from January to June in full please or type in 'all' to view for all 6 months")
        month = input ("Enter the month of your choice: ").lower()

        if month not in MONTH_DATA.keys():
                print("please enter a valid month from january to june or type 'all' to analyze all months")

    print("\nYou have chosen to analyze data for {}".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in DAY_DATA:
        print("\nWhich day of the would you like analyze data for?")
        print('-'*50)
        print("\nEnter the name of any day of the week in full e.g Monday. or type 'all' to see data for all days of the week")
        day = input ("Type here: ").lower()

        if day not in DAY_DATA:
            print("\n\nI don't understand your input. Please enter day of the week e.g Wednesday or type all to see data for all days.")
            print("Try again\n")

    print("You will be analyzing data for {} City, {} and {} as day(s)".format(city.title(), month.title(), day.title()))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load data into dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Common Day Of The Week:', popular_day)

    # TO DO: display the most common start hour

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['month'].mode()[0]

    print('Most Common Start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Common End Station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    #first combine both stations (idea from https://stackoverflow.com/questions/51635290/pandas-combine-two-columns)
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combination = df['combination'].mode()[0]
    print('Most Common Start to End Station Combination:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total time for all trips is: {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The total time for all trips is: {}".format(total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("\nWe have the following type and number of users respectively\n")
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("\n There is no gender information for this city")
    else:
        gender_count = df['Gender'].value_counts()
        print("\nWe have the following gender count in this city\n")
        print(gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("\n There is no year of birth information for this city")
    else:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        popular_year = df['Birth Year'].mode()[0]
        print("\nThe Earliest Year of Birth for this city is {}\n".format(earliest_year))
        print("\nThe Most Recent Year of Birth for this city is {}\n".format(recent_year))
        print("\nThe Most Common Year of Birth for this city is {}\n".format(popular_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #Function to display 5 rows of raw data
def data_display(df):
    """Displays raw csv files of the data on user prompt.
     user is prompted to enter 1 or 2 equivalent

     to yes or no respectively
    """


    rdata = ''
    count = 0
# loop to determine if user wants to see the raw data that was analyzed
    while True:
        print("\nDo you wish to view the raw data?\nType '1' for YES and '2' for NO")
        rdata = int(input("Enter number here: "))
        if rdata == 1:
            rdata = 'yes'
            print(df[count:count+5])
            break
        elif rdata == 2:
            rdata = 'no'
            break
        else:
            print("\nKindly Enter appropriate number please")

#loop to determine whether user wants to see more data or not
    while rdata == 'yes':
        print("\nDo you want to see more raw data?")
        count += 5
        rdata = input("\nPlease type '1' for YES or '2' for NO here: ")
         if rdata == 1:
            rdata = 'yes'
            print(df[count:count+5])
            break
        elif rdata == 2:
            rdata = 'no'
            break
            print("\nKindly Enter an appropriate number please")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#calling all defined functions above to enable them work
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)
#prompt user to decide if he wants to run the script again
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
