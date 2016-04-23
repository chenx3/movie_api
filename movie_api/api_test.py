import unittest
import requests
import json


class apitest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # test the main page
    def test_main(self):
        # return a list of countries that is available
        url = "http://localhost:5000/"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"meow meow")

    # test the top_rated function
    def test_top_rated_typical(self):
        url = "http://localhost:5000/topratedmovies/5"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list,[])

    def test_top_rated_empty(self):
        url = "http://localhost:5000/topratedmovies/0"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list,[])

    def test_top_rated_null(self):
        url = "http://localhost:5000/topratedmovies/"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, "please enter a valid number")

    def test_top_rated_invalid1(self):
        url = "http://localhost:5000/topratedmovies/40000"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    def test_top_rated_invalid2(self):
        url = "http://localhost:5000/topratedmovies/meow"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    def test_top_rated_invalid3(self):
        url = "http://localhost:5000/topratedmovies/-1"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    def test_top_rated_invalid4(self):
        url = "http://localhost:5000/topratedmovies/!@#"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    # test favorite from a year
    def test_favorite_from_year_typical1(self):
        url = "http://localhost:5000/2016/toppicks/5"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list,[])

    def test_favorite_from_year_typical2(self):
        url = "http://localhost:5000/1995/toppicks/10"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list,[])

    def test_favorite_from_year_empty(self):
        url = "http://localhost:5000/1995/toppicks/0"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list,[])

    def test_favorite_from_year_null(self):
        url = "http://localhost:5000/1995/toppicks/"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, "please enter a valid number")

    def test_favorite_from_year_invalid1(self):
        url = "http://localhost:5000/1772/toppicks/10"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid year")

    def test_favorite_from_year_invalid2(self):
        url = "http://localhost:5000/2015/toppicks/-2"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    def test_favorite_from_year_invalid3(self):
        url = "http://localhost:5000/-5/toppicks/2"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid year")

    def test_favorite_from_year_invalid4(self):
        url = "http://localhost:5000/2014/toppicks/-7"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server,"please enter a valid number")

    def test_favorite_from_year_invalid5(self):
        url = "http://localhost:5000/2014/toppicks/#@!"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    # test recent_release
    def test_recent_release_typical1(self):
        url = "http://localhost:5000/recentrelease/5"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_recent_release_typical2(self):
        url = "http://localhost:5000/recentrelease/10"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_recent_release_empty(self):
        url = "http://localhost:5000/recentrelease/0"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_recent_release_null(self):
        url = "http://localhost:5000/recentrelease/"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    def test_recent_release_invalid1(self):
        url = "http://localhost:5000/recentrelease/-5"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    def test_recent_release_invalid2(self):
        url = "http://localhost:5000/recentrelease/3000"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    def test_recent_release_invalid3(self):
        url = "http://localhost:5000/recentrelease/&*&"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    # test top rated in genre
    def test_toprated_in_genre_typical1(self):
        url = "http://localhost:5000/horror/5"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_toprated_in_genre_typical2(self):
        url = "http://localhost:5000/drama/10"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_toprated_in_genre_upper(self):
        url = "http://localhost:5000/Animation/10"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_toprated_in_genre_null(self):
        url = "http://localhost:5000/"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid number")

    def test_toprated_in_genre_empty(self):
        url = "http://localhost:5000/drama/0"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_toprated_in_genre_invalid1(self):
        url = "http://localhost:5000/drama/"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "too few argument")

    def test_toprated_in_genre_invalid2(self):
        url = "http://localhost:5000/drama/"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "too few argument")

    def test_toprated_in_genre_invalid3(self):
        url = "http://localhost:5000/132"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "too few argument")

    def test_toprated_in_genre_invalid4(self):
        url = "http://localhost:5000/sfdwere/rwe"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter valid arguments")

    def test_toprated_in_genre_invalid5(self):
        url = "http://localhost:5000/drama/12ds"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter valid arguments")

    # test title contains function
    def test_title_contains_typical1(self):
        url = "http://localhost:5000/titlecontains?query=the+revenant"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_title_contains_typical2(self):
        url = "http://localhost:5000/titlecontains?query=godfather"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_title_contains_typical3(self):
        url = "http://localhost:5000/titlecontains?query=avatar"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_title_contains_empty(self):
        url = "http://localhost:5000/titlecontains?query=sfdjlkwejrwlerk1213r"
        data_from_server = requests.get(url).text
        movie_list = json.loads(data_from_server)
        self.assertEqual(movie_list, [])

    def test_title_contains_invalid1(self):
        url = "http://localhost:5000/titlecontains?"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid argument")

    def test_title_contains_invalid2(self):
        url = "http://localhost:5000/titlecontains?"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid argument")

    def test_title_contains_invalid3(self):
        url = "http://localhost:5000/titlecontains?dswe"
        data_from_server = requests.get(url).text
        self.assertEqual(data_from_server, "please enter a valid argument")


if __name__ == '__main__':
    unittest.main()