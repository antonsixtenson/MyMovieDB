import sqlite3

class MovieDB():

    def __init__(self):
        self.db = sqlite3.connect("movies.db")
        self.c = self.db.cursor()

    def init_movies_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS movies(
                id INTEGER NOT NULL PRIMARY KEY,
                title TEXT,
                rating INTEGER,
                date_seen INTEGER,
                genre INTEGER,
                FOREIGN KEY (genre) REFERENCES genre(id)
            )
        ''')
        self.db.commit()

    def init_series_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS series(
                id INTEGER NOT NULL PRIMARY KEY,
                title TEXT,
                rating INTEGER,
                date_seen INTEGER,
                genre TEXT,
                FOREIGN KEY (genre) REFERENCES genre(id)
            )
        ''')
        self.db.commit()

    def init_genre_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS genres(
                id INTEGER NOT NULL PRIMARY KEY,
                genre TEXT
            )
        ''')
        self.db.commit()

    def save_movie(self, title, rating, date, genre=None):
        if(self.check_movie_double(title)):
            self.c.execute('''INSERT INTO movies(title, rating, date_seen, genre) VALUES(?, ?, ?, ?)''', (title.lower(), rating, date, genre))
            self.db.commit()
            return True
        else:
            return False

    def save_series(self, title, rating, date, genre=None):
        if(self.check_series_double(title)):
            self.c.execute('''INSERT INTO series(title, rating, date_seen, genre) VALUES(?, ?, ?, ?)''', (title.lower(), rating, date, genre))
            self.db.commit()
            return True
        else:
            return False



    def input_genre(self, genre):
        if(self.check_genre_double(genre)):
            self.c.execute('''INSERT INTO genres(genre) VALUES(?)''', (genre.lower(),))
            self.db.commit()
            return True
        else:
            return False

    def fetch_genre_id_by_name(self, genre):
        self.c.execute('''SELECT id FROM genres WHERE genre=?''', (genre.lower(),))
        id_ = self.c.fetchone()
        if(not id_):
            self.input_genre(genre)
            return self.fetch_genre_id_by_name(genre)
        else:
            return id_[0]


    def check_genre_double(self, genre):
        self.c.execute('''SELECT genre FROM genres WHERE genre=?''', (genre.lower(),))
        if(not self.c.fetchone()):
            return True
        else:
            return False

    def check_movie_double(self, title):
        self.c.execute('''SELECT title FROM movies WHERE title=?''', (title.lower(),))
        if(not self.c.fetchone()):
            return True
        else:
            return False

    def check_series_double(self, title):
        self.c.execute('''SELECT title FROM series WHERE title=?''', (title.lower(),))
        if(not self.c.fetchone()):
            return True
        else:
            return False

    def init_full_db(self):
        self.init_genre_table()
        self.init_series_table()
        self.init_movies_table()

