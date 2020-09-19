class ReadFile():
    def __init__(self, file_name):
        self.file_name = file_name

    def file_to_string(self):
        file = open(self.file_name)
        file_as_string = ""
        for line in file.readlines():
            file_as_string += line
        file.close()

        file_as_string = ' '.join(file_as_string.split())
        return file_as_string
