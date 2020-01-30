import sqlite3
import pandas as pd


class _DB():
    def __init__(self):
        # Establish connection with database
        sqlite_db = '../database/recipes_db.sqlite'
        self.conn = sqlite3.connect(sqlite_db)
        self.c = self.conn.cursor()
        # self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # print(self.c.fetchall())

    def set_params(self, search_params):
        self.main = search_params['main']
        self.dietary = search_params['dietary']
        self.time2cook = search_params['time2cook']

    def get_all(self):
        sql = ('SELECT * FROM RECIPES  '
               f'WHERE duration_seconds <= {self.time2cook} ')

        if self.main is not False and self.main.lower() != 'false':
            sql = sql + f'AND ingredients LIKE "%{self.main}%" '
        if self.dietary is not False and self.dietary.lower() != 'false':
            sql = sql + f'AND tags LIKE "%{self.dietary}%" '

        recipes = pd.read_sql(sql, con=self.conn, index_col='index')
        if recipes.ingredients.count() == 0:
            recipes = None

        return recipes


class API():
    def __init__(self):
        self.db = _DB()
        self.history = []

    def set_search_params(self, search_params):
        self.db.set_params(search_params)

    def reset_history(self):
        self.history = []

    def register_liked(self):
        pass

    def register_disliked(self):
        pass

    def get_next_recipe(self):

        # If its the first ask
        if len(self.history) == 0:
            self.recipes = self.db.get_all()
            # If there are no matches return None
            if self.recipes is None:
                self.record = None
                return self.record
            # If there are matches shuffle the order
            elif self.recipes is not None:
                self.recipes = self.recipes.sample(frac=1)
                self.n_results = len(self.recipes)

        # If bot has not returned all possible options
        if len(self.history) < self.n_results:
            single_recipe = self.recipes.iloc[len(self.history)]
            self.record = single_recipe.to_dict()
            self.record['id'] = single_recipe.name
            self.history.append(self.record['id'])
        # If returned all options send 'End'
        elif len(self.history) >= self.n_results:
            self.record = 'End'

        return self.record

    def get_current_recipe(self):
        return self.record
