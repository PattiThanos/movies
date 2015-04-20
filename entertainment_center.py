#import fresh_tomatoes.py is the interface of the movies website. It generates HTML, applies styles, dynamically
#generates content and much more. #import media.py contains the parent class Movie() and its contents
import fresh_tomatoes
import media

#create an object or instance of class Movie()
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
#create an object or instance of class Movie()
avatar = media.Movie("Avatar",
                     "A story of a marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser_Post",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
#create an object or instance of class Movie(), it takes 4 arguments
titanic = media.Movie("Titanic",
                      "A story about a ship that sinks",
                      "http://upload.wikimedia.org/wikipedia/commons/3/36/Titanic-Cobh-Harbour.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
#titanic.show_trailer()
#create an object or instance of class Movie(), it takes 4 arguments
school_of_rock = media.Movie("School of Rock",
                             "Storyline for School of Rock",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
#create an object or instance of class Movie(), it takes 4 arguments
ratatouille = media.Movie("Ratatouille",
                          "Storyline for Ratatouille",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
#create an object or instance of class Movie(), it takes 4 arguments
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline for Midnight in Paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")
#create an object or instance of class Movie(), it takes 4 arguments
hunger_games = media.Movie("Hunger Games",
                           "Storyline for Hunger Games",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

#Array of movie objects
movies = [toy_story, titanic,school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
