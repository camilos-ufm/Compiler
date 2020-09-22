import objects.Symbol as Symbol

class Scanner:
    
    def holaScanner(self):
        print("DESDE SCANNER")

    def scan(self, input_string):
        for object_list in input_string:
            for word in object_list[0].split(" "):
                print(word, object_list[1])