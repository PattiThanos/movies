import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #init is a function or constructor. Self refers to movie object
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #initialize movie variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #define function to open browser and play video
    #this is an instance method because it is defined inside a class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



