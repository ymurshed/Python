from MovieData import MovieData
from collections import Counter


class Output:

    top_actor_list = []
    top_director_list = []
    top_actor_list_with_movies = {}
    top_rating_from_unwatched_movies = {}

    def create_top_actor_list(self, dic, i=10):
        md = MovieData()

        for k, v in dic.items():
            md = v
            for actor in md.actors:
                self.top_actor_list.append(actor)

        '''returns tuple'''
        top_i_actors = Counter(self.top_actor_list).most_common(i)
        self.top_actor_list.clear()

        for actor in top_i_actors:
            self.top_actor_list.append(actor[0])

    def create_top_director_list(self, dic, i=10):
        md = MovieData()

        for k, v in dic.items():
            md = v
            for director in md.directors:
                self.top_director_list.append(director)

        '''returns tuple'''
        top_i_directors = Counter(self.top_director_list).most_common(i)
        self.top_director_list.clear()

        for director in top_i_directors:
            self.top_director_list.append(director[0])

        return self.top_director_list

    def create_top_actor_list_with_movie_title(self, dic, i=10):
        md = MovieData()
        self.create_top_actor_list(dic, i)

        for actor in self.top_actor_list:
            movie_name = []
            for k, v in dic.items():
                md = v
                if actor in md.actors:
                    movie_name.append(md.movie_title)
            self.top_actor_list_with_movies[actor] = movie_name

        return self.top_actor_list_with_movies

    def get_min_from_top_10_rating_from_watchedlist(self, dic, i):
        md = MovieData()
        top_i_rating = []

        for k, v in dic.items():
            md = v
            if md.imdb_rating not in top_i_rating:
                top_i_rating.append(md.imdb_rating)
        top_i_rating.sort(reverse=True)

        return min(top_i_rating[:i])

    def top_rated_in_unwatchedlist(self, watched_dic, unwatched_dic, i=10):
        md = MovieData()
        rating = self.get_min_from_top_10_rating_from_watchedlist(watched_dic, i)

        for k, v in unwatched_dic.items():
            md = v
            if md.imdb_rating >= rating:
                self.top_rating_from_unwatched_movies[md.movie_title] = md.imdb_rating

        return rating, self.top_rating_from_unwatched_movies
