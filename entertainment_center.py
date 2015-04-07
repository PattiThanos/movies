import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A story of a marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser_Post",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
titanic = media.Movie("Titanic",
                      "A story about a ship that sinks",
                      "http://upload.wikimedia.org/wikipedia/commons/3/36/Titanic-Cobh-Harbour.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
#titanic.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Storyline for School of Rock",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                          "Storyline for Ratatouille",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline for Midnight in Paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")
hunger_games = media.Movie("Hunger Games",
                           "Storyline for Hunger Games",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, titanic,school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
