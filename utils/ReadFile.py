from re import match

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
                    cx = 0
                    for char in string_line:
                        if(char=="+" or char=="=" or char=="-" or char=="<" or char==">" or char=="!"):
                            # print("char", char)
                            try:
                                if(char=='+'):
                                    if(string_line[cx-1] != '+'):
                                        string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                        cx += 1
                                    if(string_line[cx+1] != '+' and string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1
                                if(char=='='):
                                    if(string_line[cx-1] != '=' and string_line[cx-1] != '+' and string_line[cx-1] != '-' and string_line[cx-1] != '<' and string_line[cx-1] != '>' and string_line[cx-1] != '!'):
                                        string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                        cx += 1
                                    if(string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1  
                                if(char=='-'):
                                    if(string_line[cx-1] != '-'):
                                        string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                        cx += 1
                                    if(string_line[cx+1] != '-' and string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1
                                if(char=='<'):
                                    
                                    string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                    cx += 1

                                    if(string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1

                                if(char=='>'):
                                    string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                    cx += 1

                                    if(string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1

                                if(char=='!'): 
                                    string_line = string_line = string_line[:cx] + " " + string_line[cx] + string_line[cx + 1:]
                                    cx += 1

                                    if(string_line[cx+1] != '='):
                                        string_line = string_line = string_line[:cx] + string_line[cx] + " " + string_line[cx + 1:]
                                        cx += 1
                                # if(string_line[string_line.index(char)+1] != "+" and string_line[string_line.index(char)+1] != "=" and string_line[string_line.index(char)+1] != "-" 
                                # and string_line[string_line.index(char)-1] != "+"  and string_line[string_line.index(char)-1] != "-" and string_line[string_line.index(char)-1] != ">" and
                                # string_line[string_line.index(char)-1] != "<" and string_line[string_line.index(char)-1] != "=" and string_line[string_line.index(char)-1] != "!") :
                                    # print("cx",string_line[cx])
                                    # print(string_line[string_line.index(char)+1])
                                    # print(string_line[string_line.index(char)-1])
                                    # print("ccx", cx)
                                    # string_line = string_line[:cx] + " " + string_line[cx] + " " + string_line[cx + 1:]
                                    # cx+=2
                                    #string_line = string_line.replace(string_line[string_line.index(char)], " "+string_line[string_line.index(char)]+" ")
                                # print(string_line)
                            except Exception:
                                print(Exception)
                            else:
                                pass
                        cx+=1
                    for char in string_line:
                        if(char=="&" or char=="%" or char=="/"
                            or char=="*" or char=="(" or char==")" or char=="{" or char=="}" or char==";" or char==","):
                            string_line = string_line.replace(string_line[string_line.index(char)], " "+string_line[string_line.index(char)]+" ")
                        
                    
                    if("+=" in string_line):
                        string_line = string_line.replace("+=", " += ")
                    elif("==" in string_line):
                        string_line = string_line.replace("==", " == ")
                    elif("-=" in string_line):
                        string_line = string_line.replace("-=", " -= ")                    
                    elif("<=" in string_line):
                        string_line = string_line.replace("<=", " <= ")  
                    elif(">=" in string_line):
                        string_line = string_line.replace(">=", " >= ")  
                    elif("!=" in string_line):
                        string_line = string_line.replace("!=", " != ")  
                    elif("||" in string_line):
                        string_line = string_line.replace("||", " || ")  
                    elif("++" in string_line):
                        string_line = string_line.replace("++", " ++ ")
                    elif("--" in string_line):
                        string_line = string_line.replace("--", " -- ")
                    string_line = ' '.join(string_line.split())
                    if(string_line!=""):
                        file_as_string_list.append([string_line, count])
                count+=1
            file.close()
            if(flag_comment==True):
                file_as_string_list = []
                print("Lexical error: Bad comment, missing closing */")
        return file_as_string_list
