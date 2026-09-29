import pandas as pd
import numpy as np

def process_data(csv_file):
    df = pd.read_csv(csv_file)

    # df['passholder_type'] = df['passholder_type'].replace(['nan', 'NaN', '', 0], pd.NA)

    df = df = df[~((df['bike_type'] == 'smart') | df['passholder_type'].isnull())]
    # adding revenue column based on duration and passholder_type
    # does not include flat rate for buying pass and 24-hour $5 start fee
    # one Day Pass
    # walk up
    # monthly Pass
    # annual
    passes = [
        (df['passholder_type'] == 'Walk-up'),
        (df['passholder_type'] == 'One Day Pass'),
        (df['passholder_type'] == 'Monthly Pass'), 
        (df['passholder_type'] == 'Annual Pass')
    ]
    revenues = [
        3.5 * df['duration'],
        (3.5 * df['duration']) - 1.75,
        (3.5 * df['duration']) - 1.75,
        (3.5 * df['duration']) - 1.75,
    ]

    df['revenue'] = np.select(passes, revenues, default=0)

    # adding $1.00 to revenue for electric bikes
    electric_bikes = df['bike_type'] == 'Electric'
    df.loc[electric_bikes, 'revenue'] += 1

    # adding bike type and passholder pair column
    df['bike_pass_pair'] = df['bike_type'] + ',' + df['passholder_type']
    
    return df.to_csv("final.csv", index=False)