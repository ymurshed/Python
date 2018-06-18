import os


class SearchWord:

    searching_path = 'E:\Code\Programming_Hub\Python\WordSearching\input files'   #path is currently hardcoded, will change later on
    searching_text = ''

    files = []
    file_extension = ['.txt']   #['.txt', '.doc', '.docx', '.pdf']
    report = {}

    def __init__(self):
        print('!!!This program is for finding a given text from a directory!!!')

    def take_input(self):
        print('Enter the text you want to search: ')
        self.searching_text = input()

    def populate_file_list(self):
        print('Populating file list...')

        for filename in os.listdir(self.searching_path):
            name, ext = os.path.splitext(filename)

            if any(e in ext for e in self.file_extension):
                self.files.append(os.path.join(self.searching_path, filename))

    def find_text_in_files(self):
        print('Start finding text...')

        for file in self.files:
            list_value = []

            with open(file, "r") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                if self.searching_text in line:
                    res = 'line #' + str(i + 1) + " : " + line
                    list_value.append(res)

            if list_value:
                self.report[file] = list_value

    def generate_report(self):
        print('Generating report...')

        if not self.report:
            print('(' + self.searching_text + ') not found!!!')

        for key, value in self.report.items():
            print("In file (" + key + ") the given text (" + self.searching_text + ") found in following lines:")
            print(value)


if __name__ == "__main__":
    ob = SearchWord()

    ob.take_input()
    ob.populate_file_list()
    ob.find_text_in_files()
    ob.generate_report()
