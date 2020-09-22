class ReadFile():
    def __init__(self):
        self.file_name = ""

    def set_file(self, file_name):
        self.file_name = file_name
        
    def file_to_string(self):
        file_as_string_list = []
        try:
            file = open(self.file_name)
        except FileNotFoundError:
            print("Wrong file or file path")
        else:
            # remove comments from input string 
            flag_comment = False
            count = 1
            for line in file.readlines():
                if("//" in line and flag_comment==False):
                    #print(type(line.find("//")))
                    string_line = line.replace(line[line.find("//"):-1],"")
                    string_line = ' '.join(string_line.split())
                    if(string_line!=""):
                        file_as_string_list.append([string_line, count])
                elif("/*" in line):
                    flag_comment = True
                elif("*/" in line):
                    flag_comment = False
                elif(flag_comment==False):
                    string_line = line
                    string_line = ' '.join(string_line.split())
                    if(string_line!=""):
                        file_as_string_list.append([string_line, count])
                count+=1
            file.close()
            if(flag_comment==True):
                file_as_string_list = []
                print("bad comment")
        return file_as_string_list
