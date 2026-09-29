import pandas as pd
import numpy as np

def process_data():
    df = pd.read_csv('rental_bike_data.csv')

    df['passholder_type'] = df['passholder_type'].replace(['nan', 'NaN', ''], pd.NA)
    df['passholder_type'] = df['passholder_type'].astype(str).str.strip().str.lower()

    df = df[~df['passholder_type'].isna() & (df['passholder_type'] != 'testing')].copy()

    # adding revenue column based on duration and passholder_type
    # does not include flat rate for buying pass and 24-hour $5 start fee
    # one Day Pass
    # walk up
    # monthly Pass
    # annual
    passes = [
        (df['passholder_type'] == 'walk-up'),
        (df['passholder_type'] == 'one day pass'),
        (df['passholder_type'] == 'monthly pass'), 
        (df['passholder_type'] == 'annual pass')
    ]
    revenues = [
        3.5 * df['duration'],
        (3.5 * df['duration']) - 1.75,
        (3.5 * df['duration']) - 1.75,
        (3.5 * df['duration']) - 1.75,
    ]

    df['revenue'] = np.select(passes, revenues, default=0)


    # adding bike type and passholder pair column
    df['bike_pass_pair'] = df['bike_type'] + ',' + df['passholder_type']
    print(df.head(10))
