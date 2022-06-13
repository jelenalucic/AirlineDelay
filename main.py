import pandas as pd


def main():
    df = pd.read_csv('res/2014.csv')

    # df = df.append(pd.read_csv('res/2015.csv'))
    # df = df.append(pd.read_csv('res/2016.csv'))
    # df = df.append(pd.read_csv('res/2017.csv'))
    # df = df.append(pd.read_csv('res/2018.csv'))

    average_arrival_delay_time = df['ARR_DELAY'].mean()
    print(f"Average delay time for a period 2014-2018: {average_arrival_delay_time}")

    median_arrival_delay_time = df['ARR_DELAY'].median()
    print(f"Median delay time for a period 2014-2018: {median_arrival_delay_time}")

    print("\n\nAverage and median delay time per Year:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df['FL_DATE'] = pd.to_datetime(df['FL_DATE'])
    df['FL_DATE_YEAR'] = df['FL_DATE'].dt.to_period('Y')
    df = df.rename(columns={'FL_DATE_YEAR': 'Year'})
    year_dataframe = df.groupby(df['Year']).agg(functions)
    print(year_dataframe)

    # df['FL_DATE'] = pd.to_datetime(df['FL_DATE'])
    # df['FL_DATE_YEAR'] = df['FL_DATE'].dt.to_period('Y')
    # year_dataframe = df.groupby(df['FL_DATE_YEAR'])
    # year_dataframe = year_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # print(year_dataframe)

    print("\n\nAverage and median delay time per quarter:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df['FL_DATE_QUARTER'] = df['FL_DATE'].dt.to_period('Q')
    df = df.rename(columns={'FL_DATE_QUARTER': 'Quarter'})
    quarter_dataframe = df.groupby(df['Quarter']).agg(functions)
    print(quarter_dataframe)

    # df['FL_DATE_QUARTER'] = df['FL_DATE'].dt.to_period('Q')
    # quarter_dataframe = df.groupby(df['FL_DATE_QUARTER'])
    # quarter_dataframe = quarter_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # print(quarter_dataframe)

    print("\n\nAverage and median delay time per month:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df['FL_DATE_MONTH'] = df['FL_DATE'].dt.to_period('M')
    df = df.rename(columns={'FL_DATE_MONTH': 'Month'})
    month_dataframe = df.groupby(df['Month']).agg(functions)
    print(month_dataframe)

    # df['FL_DATE_MONTH'] = df['FL_DATE'].dt.to_period('M')
    # month_dataframe = df.groupby(df['FL_DATE_MONTH'])
    # month_dataframe = month_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # print(month_dataframe)

    print("\n\nAverage and median delay time per week:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df['FL_DATE_WEEK'] = df['FL_DATE'].dt.to_period('W')
    df = df.rename(columns={'FL_DATE_WEEK': 'Week'})
    week_dataframe = df.groupby(df['Week']).agg(functions)
    print(week_dataframe)

    # df['FL_DATE_WEEK'] = df['FL_DATE'].dt.to_period('W')
    # week_dataframe = df.groupby(df['FL_DATE_WEEK'])
    # week_dataframe = week_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # print(week_dataframe)

    print("\n\nAverage and median delay time per day:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df['FL_DATE_DAY'] = df['FL_DATE'].dt.to_period('D')
    df = df.rename(columns={'FL_DATE_DAY': 'Day'})
    day_dataframe = df.groupby(df['Day']).agg(functions)
    print(day_dataframe)

    # df['FL_DATE_DAY'] = df['FL_DATE'].dt.to_period('D')
    # day_dataframe = df.groupby(df['FL_DATE_DAY'])
    # day_dataframe = day_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # print(day_dataframe)

    print("\n\nAverage and median delay time per carrier:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df = df.rename(columns={'OP_CARRIER': 'Carrier'})
    carrier_dataframe = df.groupby(df['Carrier']).agg(functions)
    print(carrier_dataframe)

    # carrier_dataframe = df.groupby(df['OP_CARRIER'])
    # carrier_dataframe = carrier_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')

    print("\n\nAverage and median delay time per origin:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df = df.rename(columns={'ORIGIN': 'Origin'})
    origin_dataframe = df.groupby(df['Origin']).agg(functions)
    print(origin_dataframe)

    # origin_dataframe = origin_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')

    print("\n\nAverage and median delay time per destination:\n")
    functions = {'ARR_DELAY': ['mean', 'median']}
    df = df.rename(columns={'DEST': 'Destination'})
    destination_dataframe = df.groupby(df['Destination']).agg(functions)
    print(destination_dataframe)

    # destination_output_dataframe = destination_dataframe['ARR_DELAY'].mean().reset_index(name='Average time delay')
    # destination_output_dataframe['Median time delay'] = destination_dataframe['ARR_DELAY'].median()


if __name__ == '__main__':
    main()

