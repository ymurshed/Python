class Helper:

    @staticmethod
    def split_string_to_list(item_values):
        items = str(item_values)
        items = items.split(";")
        items = [x.strip(' ') for x in items]
        return items

    @staticmethod
    def write_xml_file(file, tree):
        with open(file, "w") as f:
            f.write(tree)
            f.close()
        print('Form mapping xml writing completed!')

    @staticmethod
    def print_all(self):
        for k, v in self.qcat_item_names.items():
            print(k, v)

        for k, v in self.sf_item_names.items():
            print(k, v)

        for k, v in self.qcat_item_values.items():
            print(k, v)

        for k, v in self.sf_item_values.items():
            print(k, v)
