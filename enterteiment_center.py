import media
import fresh_tomatoes

#Class Movie contents: movie_title, story_line, poster_image, youtube_trailer)
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his that come to live.",
                        "http://wallpapersdsc.net/wp-content/uploads/2015/11/136.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

a_beautifull_mind = media.Movie("A beautifull Mind",
                                "A mathematician genius who has 3 persons living in his head.",
                                "http://static.cinemarx.ro/poze/postere/filme/2001/A-Beautiful-Mind-1542-284.jpg",
                                "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

movies = [toy_story, a_beautifull_mind]
print(media.Movie.__name__)
print(media.Movie.__module__)
#fresh_tomatoes.open_movies_page(movies)