import objects.Symbol as Symbol

class Scanner:
    #symbol list cons
    SYMBOL_LIST = []
    SYMBOL_LIST.append(Symbol.Symbol(1, "holaname", "holaregex"))
    # TODO

    def holaScanner(self):
        print("DESDE SCANNER")

    def scan(self, input_string):
        for object_list in input_string:
            for word in object_list[0].split(" "):
                print(word, object_list[1])

        print(self.SYMBOL_LIST[0].regEx)