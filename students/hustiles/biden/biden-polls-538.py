# Get latest Biden trends from 538
# https://projects.fivethirtyeight.com/biden-approval-rating

import pandas as pd

# Read csv file
url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
src = pd.read_csv(url)


# Rename columns
src.rename(columns={'modeldate':'date', 'approve_estimate':'approve', 'disapprove_estimate':'disapprove'} , inplace=True)


# Clean up approval/disapproval and calculate difference
src['spread'] = src['approve'] - src['disapprove']
src['disapprove'] = src['disapprove'].round(2)
src['approve'] = src['approve'].round(2)
src['spread'] = src['spread'].round(2)


# Process dates
src['datetime'] = pd.to_datetime(src['timestamp'])
src['date'] = src['datetime'].dt.strftime('%m-%d-%y')
src['date_display'] = src['datetime'].dt.strftime('%b. %d')


# Make sure we don't have duplicates
src.drop_duplicates(subset=['date', 'subgroup'], keep='last', inplace=True)


# Make a copy of the dataframe with only polls of "adults"
df = src[src['subgroup'] == 'Adults'].copy()


# Export
df.to_csv('data/processed/biden_polls_adults.csv')