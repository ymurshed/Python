from FileAccess import FileAccess
from OMDBApi import OMDBApi
from Show import Show
from Output import Output


if __name__ == "__main__":

    print('Please wait for around 30 mins! It will take sometimes while getting data from OMDB API calling.....')
    print('If you want to run the program with less data to avoid delay then please minimize the contents of '
          'inputs folder and re-run!!!\n')

    show = Show()
    unwatched_movie_dic = {}

    try:
        '''read input text file'''
        fa = FileAccess()
        movie_list = fa.read_file(fa.movie_list_txt)
        watched_movie_list = fa.read_file(fa.watched_movie_list_txt)
        unwatched_movie_list = set(movie_list) - set(watched_movie_list)

        '''print movie, watched and unwatched movie id'''
        '''
        print('-----------> Movie Id: ')
        show.print_input_list(movie_list)
        print('-----------> Watched Movie Id: ')
        show.print_input_list(watched_movie_list)
        print('-----------> Unwatched Movie Id: ')
        show.print_input_list(unwatched_movie_list)
        '''

        '''call OMDB api and load movie related data'''
        api = OMDBApi()
        movie_dic = api.call_omdb_api(movie_list)
        watched_movie_dic = api.call_omdb_api(watched_movie_list)

        for movie_id in unwatched_movie_list:
            unwatched_movie_dic[movie_id] = movie_dic[movie_id]

        '''print movie, watched and unwatched movie data'''
        '''
        print('-----------> Movie Information: ')
        show.print_input_dictionary(movie_dic)
        print('-----------> Watched Movie Information: ')
        show.print_input_dictionary(watched_movie_dic)
        print('-----------> Unwatched Movie Information: ')
        show.print_input_dictionary(unwatched_movie_dic)
        '''

        '''output'''
        op = Output()
        top_actor_list_with_movies = op.create_top_actor_list_with_movie_title(movie_dic)
        top_director_list = op.create_top_director_list(movie_dic)
        rating, top_rating_from_unwatched_movies = op.top_rated_in_unwatchedlist(watched_movie_dic, unwatched_movie_dic)

        result = ''
        result += show.print_top_actor_with_movies(top_actor_list_with_movies) + '\n'
        result += show.print_top_director(top_director_list) + '\n'
        result += show.print_top_rated_from_unwatched(rating, top_rating_from_unwatched_movies) + '\n'

        '''write final output to the file'''
        fa.write_file(fa.required_output_txt, result)
        print('Thank you for waiting! Output is written to the outputs folder!')

    except Exception as e:
        print('Program error!!! Error message: ' + str(e))


