from MovieData import MovieData


class Show:

    def print_input_list(self, list):
        res = ''

        for v in list:
            res += v + '\n'
        print(res)

    def print_input_dictionary(self, dic):
        res = ''
        md = MovieData()

        for k, v in dic.items():
            md = v
            res += k + '\n'
            res += md.movie_title + '\n'
            res += ' '.join(md.actors)
            res += '\n'
            res += ' '.join(md.directors)
            res += '\n'
            res += str(md.imdb_rating) + '\n'
        print(res)

    def print_top_actor_with_movies(self, dic):
        i = 0
        res = 'My top 10 favorite actors including the movie titles:\n'

        for k, v in dic.items():
            i += 1
            j = 0
            res += str(i) + ') Actor: ' + k + ', Movie Titles: '

            for movie in v:
                j += 1
                res += movie

                if j <= len(v) - 1:
                    res += ' ~ '
            res += '\n'

        return res

    def print_top_director(self, list):
        i = 0
        res = 'My top 10 favorite movie directors:\n'

        for v in list:
            i += 1
            res += str(i) + ') Director: ' + v + '\n'

        return res

    def print_top_rated_from_unwatched(self, rating, dic):
        i = 0
        res = 'Top rated movies I should watch from my unwatched collection (base condition: rating should be >= ' \
              + str(rating) + '):\n'

        for k, v in dic.items():
            i += 1
            res += str(i) + ') Movie Title: ' + k + ', Rating: ' + str(v) + '\n'

        return res
