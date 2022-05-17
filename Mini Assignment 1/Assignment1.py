class StringClass:
    def __init__(self,str):
        self.str = str;

    def length_of_string(self):
        counter = 0
        for i in self.str:
            counter += 1
        return counter
    def list_of_character(self):
        chars = list(self.str)
        print(chars)

str = input("Please input string : ")
obj = StringClass(str)
print(obj.length_of_string())
obj.list_of_character()