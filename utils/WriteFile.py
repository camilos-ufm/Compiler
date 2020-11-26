from datetime import datetime

class WriteFile():
    def __init__(self):
        self.file_name = ""

    def write_file(self, file_name, string_list):
        self.file_name = file_name
        file_output = open("output/"+file_name+".txt", "w")
        for line in string_list:
            file_output.write(line+"\n")
        file_output.close()

    def write_file_no_extension(self, file_name, string_list):
        self.file_name = file_name
        file_output = open("output/"+file_name, "w")
        for line in string_list:
            file_output.write(line+"\n")
        file_output.close()

    def write_file_append(self, file_name, string_list):
        # datetime object containing current date and time
        now = datetime.now()
        
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.file_name = file_name
        file_output = open("output/"+file_name+".txt", "a")
        for line in string_list:
            file_output.write("["+dt_string+"]: " + str(line)+"\n")
        file_output.close()