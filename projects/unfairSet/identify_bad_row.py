import sqlite3
from UnfairSet.UnfairSet import UnfairSet
import collections

class Identify_bad_row():
    def __init__(self, DB_file):
        self.DB = sqlite3.connect(DB_file)
        self.DB_films_list = []
        self.DB_unfair_sets = []
        self.get_films_list()
        self.get_unfairsets_titles()
        self.identify()


    def get_films_list(self):
        for row in self.DB.execute('SELECT title FROM films'):
            self.DB_films_list.append(row[0])

    def get_unfairsets_titles(self):
        for row in self.DB.execute('SELECT title FROM unfairset'):
            self.DB_unfair_sets.append(row[0])

    def identify(self):
        for x in range(0, len(self.DB_films_list)):
            movie_title = self.DB_films_list[x]
            instance = UnfairSet(movie_title)
            converted_movie_title = instance.UnfairSet
            db_unfair_set = list(self.DB_unfair_sets[x])
            if (collections.Counter(converted_movie_title) != collections.Counter(db_unfair_set)):
                print(movie_title)

identify = Identify_bad_row('film.sqlite')