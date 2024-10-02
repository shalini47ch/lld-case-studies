class Movie:
    def __init__(self, title, genre, language, release_date, duration):
        self.title=title
        self.genre=genre
        self.language=language
        self.release_date=release_date
        self.duration=duration
        self.shows=[]
    
    #now here we create the getter and the setter functions
    def get_title(self):
        return self.title
    
    def get_genre(self):
        return self.genre
    
    def get_language(self):
        return self.language
    
    def get_releasedate(self):
        return self.release_date
    
    def get_duration(self):
        return self.duration
    
    def get_shows(self):
        return self.shows

movie=Movie("Annabelle","Horror","English","21 july","3hr")
print(movie.get_genre())
print(movie.get_language())
print(movie.get_duration())
        