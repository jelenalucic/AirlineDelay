import pandas as pd


def main():
    df = pd.read_csv('res/2014.csv')
    arrival_delay_column = df['ARR_DELAY']

    average_arrival_delay_time = arrival_delay_column.mean()
    print(f"Average delay time in 2014: {average_arrival_delay_time}")

    median_arrival_delay_time = arrival_delay_column.median()
    print(f"Median delay time in 2014: {median_arrival_delay_time}")

    df['FL_DATE'] = pd.to_datetime(df['FL_DATE'])
    df['FL_DATE_QUARTER'] = df['FL_DATE'].dt.to_period('Q')
    quarter_dataframe = df.groupby(df['FL_DATE_QUARTER'])
    quarter_dataframe = quarter_dataframe['ARR_DELAY'].mean()
    print(quarter_dataframe)

    # df = df.append(pd.read_csv('res/2015.csv'))
    # df = df.append(pd.read_csv('res/2016.csv'))
    # df = df.append(pd.read_csv('res/2017.csv'))
    # df = df.append(pd.read_csv('res/2018.csv'))


if __name__ == '__main__':
    main()

