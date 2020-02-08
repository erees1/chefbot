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

    def get_all(self, search_params):
        main = search_params['main']
        dietary = search_params['dietary']
        time2cook = search_params['time2cook']

        sql = ('SELECT * FROM RECIPES  ')

        if self.is_specified(time2cook):
            time2cook_v = int(time2cook['value'])
            query = [f'duration_seconds <= {time2cook_v}']
            sql = self.add_query(sql, query)

        if self.is_specified(main):
            main_queries = [main]
            if main[-1] == 's':
                main_queries.append(main[:-1])

            query = [
                f'(ingredients LIKE "%{main}%" OR dish LIKE "%{main}%")'
                for main in main_queries
            ]
            sql = self.add_query(sql, query)

        if self.is_specified(dietary):
            dietary = [dietary]
            if dietary[0] == 'vegeterian':
                dietary.append('vegan')

            query = [f'tags LIKE "%{d}%"' for d in dietary]
            sql = self.add_query(sql, query)
        # print(sql)
        recipes = pd.read_sql(sql, con=self.conn, index_col='index')
        if recipes.ingredients.count() == 0:
            recipes = None

        return recipes

    def add_query(self, sql, queries, logic='OR'):
        query = '(' + f' {logic} '.join(queries) + ')'
        if 'where' in sql.lower():
            sql = sql + f' AND {query} '
        elif 'where' not in sql.lower():
            sql = sql + f' WHERE {query} '
        return sql

    def is_specified(self, param):
        if param is False:
            return False
        elif param is None:
            return False
        elif isinstance(param, str) and param.lower() == 'false':
            return False
        elif isinstance(param, str) and param.lower() == 'none':
            return False
        else:
            return True


class API():
    def __init__(self):
        self.db = _DB()
        self.history = []

    def set_search_params(self, search_params):
        self.search_params = search_params

    def reset_history(self):
        self.history = []

    def register_liked(self):
        pass

    def register_disliked(self):
        pass

    def get_next_recipe(self):

        # If its the first ask
        if len(self.history) == 0:
            self.recipes = self.db.get_all(self.search_params)
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

    def are_matches(self, search_params):
        print('checking database for matches:', search_params)
        if self.db.get_all(search_params) is not None:
            return True
        else:
            return False
