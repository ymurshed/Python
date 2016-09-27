import json
from urllib.request import Request, urlopen
from MovieData import MovieData


class OMDBApi:

    temp_url = 'http://www.omdbapi.com/?i={movie_id}&plot=short&r=json'

    def call_omdb_api(self, data_list):

        dic = {}

        for movie_id in data_list:
            try:
                new_url = self.temp_url.replace("{movie_id}", movie_id)
                request = Request(new_url)

                response = urlopen(request)
                data_set = response.read().decode('utf-8')

                movie_data_set = json.loads(data_set)
                movie_object = MovieData()

                for k, v in movie_data_set.items():

                    if k == 'Title':
                        movie_object.movie_title = v
                    if k == 'Actors':
                        movie_object.actors = v.split(',')
                        movie_object.actors = [x.strip(' ') for x in movie_object.actors]
                    if k == 'Director':
                        movie_object.directors = v.split(',')
                        movie_object.directors = [x.strip(' ') for x in movie_object.directors]
                    if k == 'imdbRating':
                        movie_object.imdb_rating = float(v)

                dic[movie_id] = movie_object

            except Exception as e:
                print('No data. Got an error message: ' + str(e))

        return dic
