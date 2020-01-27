# Conver the scrapped csv to sqlite file
import sqlite3
import pandas as pd
import numpy as np
import requests
CSV_PATH = 'scraper/mob_scrape.csv'
DB_PATH = 'database/recipes_db.sqlite'

# This script creates new column called tags,
# this dict maps the website tags to tags
tags_mapper = {
    'comfort': 'comfort',
    'veggie': 'vegeterian',
    'vegan': 'vegan',
    'speedy': 'quick',
    'dinener party': 'guest',
    'guest': 'guest',
    'feed 4 for under £10': 'cheap',
    'munchies': 'snack',
    'pasta': 'pasta',
    'asian': 'asian',
}


def clean_data(recipes):
    def extract_duration(text):
        data = {'locale': 'en_GB', 'text': text}
        # Run the duration for the duckling server
        response = requests.post('http://0.0.0.0:8000/parse', data=data)

        try:
            duration = int(response.json()[0]['value']['normalized']['value'])
        except Exception:
            duration = np.nan
        return duration

    recipes.dropna(inplace=True)
    # Map the tags
    recipes['tags'] = recipes.Meta.str.lower().replace('mob', '', regex=True)
    recipes['tags'] = recipes.tags.str.strip().replace(tags_mapper, regex=True)
    recipes['tags'] = recipes.tags.map(lambda x: x
                                       if x in tags_mapper.values() else "")
    # Map the duration
    recipes['duration_seconds'] = recipes.times.map(extract_duration)
    # Make every column name lower case
    recipes.columns = recipes.columns.str.lower()

    return recipes


def save_to_sqlite(recipes):
    conn = sqlite3.connect(DB_PATH)
    # Save dataframe to sql
    recipes.to_sql('recipes', con=conn, if_exists='replace')


def main():
    recipes = pd.read_csv(CSV_PATH, index_col=0)
    recipes = clean_data(recipes)
    save_to_sqlite(recipes)


if __name__ == '__main__':
    main()
