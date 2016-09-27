class FileAccess:

    movie_list_txt = 'G:\Coding Hub\Python\IMDB\inputs\movies.txt'
    watched_movie_list_txt = 'G:\Coding Hub\Python\IMDB\inputs\watched.txt'
    required_output_txt = 'G:\Coding Hub\Python\IMDB\outputs\expected_output.txt'

    def read_file(self, file):

        list_value = []

        with open(file, "r") as f:
            lines = f.readlines()
            f.close()

        for i, line in enumerate(lines):
            list_value.append(line.rstrip())

        return list_value

    def write_file(self, file, result):

        with open(file, "w") as f:
            f.write(result)
            f.close()
