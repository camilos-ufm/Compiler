class WriteFile():
    def __init__(self):
        self.file_name = ""

    def write_file(self, file_name, string_list):
        self.file_name = file_name
        file_output = open("output/"+file_name+".txt", "w")
        for line in string_list:
            file_output.write(line+"\n")
        file_output.close()