from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import app
import datetime
from kivymd.toast import toast
from kivy.animation import Animation


class MyMovieDB(Screen):
    def __init__(self, **kwargs):
        super(MyMovieDB, self).__init__(**kwargs)
        self.sql_cursor = app.MovieDB()
        self.help_menu = False


    def save_movie(self):
        title = self.ids["movie_series"].text
        rating = self.ids["rating"].text
        date = int(str(datetime.datetime.now().date()).replace("-", ""))
        genre = self.ids["genre"].text
        genrelst = genre.split(" ")
        if(title == "" or rating == ""):
            toast("You have forgotten field/s")
        else:
            genres_id = ""
            for itm in genrelst:
                genres_id += str(self.sql_cursor.fetch_genre_id_by_name(itm)) + " "
            if(self.sql_cursor.save_movie(title, rating, date, genres_id)):
                pass
            else:
                toast("Movie already exists")
        self.ids["movie_series"].text = ""
        self.ids["rating"].text = ""
        self.ids["genre"].text = ""

    def save_series(self):
        title = self.ids["movie_series"].text
        rating = self.ids["rating"].text
        date = int(str(datetime.datetime.now().date()).replace("-", ""))
        genre = self.ids["genre"].text
        genrelst = genre.split(" ")
        if(title == "" or rating == ""):
            toast("You have forgotten field/s")
        else:
            genres_id = ""
            for itm in genrelst:
                genres_id += str(self.sql_cursor.fetch_genre_id_by_name(itm)) + " "
            if(self.sql_cursor.save_series(title, rating, date, genres_id)):
                pass
            else:
                toast("Series already exists")
        self.ids["movie_series"].text = ""
        self.ids["rating"].text = ""
        self.ids["genre"].text = ""

    def init_db(self):
        self.sql_cursor.init_full_db()
        toast("Database is now initialized, you can now add movies and series!")
        self.ids["init_db"].disabled = True

    def help(self):
        if(not self.help_menu):
            anim = Animation(pos_hint={"center_y": 0.1}, duration=0.5)
            anim.start(self.ids["help_card"])
            self.help_menu = True
        else:
            anim = Animation(pos_hint={"center_y": -0.3}, duration=0.5)
            anim.start(self.ids["help_card"])
            self.help_menu = False


class WindowManager(ScreenManager):
    pass

class ReturnMyMovieDB(MDApp):
    Window.size = (1024, 720)
    def build(self):
        wm = WindowManager()
        wm.add_widget(MyMovieDB())
        return wm
if __name__ == "__main__":
    ReturnMyMovieDB().run()

