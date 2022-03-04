import csv


class CSVFile(object):
    def __init__(self, local_file_input):
        self.local_file_input = local_file_input

    def read_csv_file(self):
        list_files = []
        try:
            with open(self.local_file_input) as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                for id, cidade, provincia, email, pec in reader:
                    dictionary = dict(
                        {"id": id, "provincia": provincia, "cidade": cidade, "email": [email, pec]}
                    )
                    list_files.append(dictionary)
                return list_files
        except Exception:
            raise

    def save_csv_file(self, json):
        with open(self.local_file_input, 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(json)
