class ReadFile():
    def __init__(self, file_name):
        self.file_name = file_name

    def file_to_string(self):
        file_as_string = ""
        try:
            file = open(self.file_name)
        except FileNotFoundError:
            print("Wrong file or file path")
        else:
            # remove comments from input string 
            for line in file.readlines():
                if("//" in line):
                    #print(type(line.find("//")))
                    file_as_string += line.replace(line[line.find("//"):-1],"")
                else:
                    file_as_string += line
            file.close()

            file_as_string = ' '.join(file_as_string.split())
            while("/*" in file_as_string):
                if("*/" in file_as_string):
                    file_as_string = file_as_string.replace(file_as_string[file_as_string.find("/*"):file_as_string.find("*/")+2],"")
                else:
                    print("bad comment")
                    file_as_string = ""
        return file_as_string
