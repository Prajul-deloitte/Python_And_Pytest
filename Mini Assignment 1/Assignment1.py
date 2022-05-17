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

class PairsPossible(StringClass):
    string = ""
    arr = []
    def __init__(self):
        self.string = input("Enter string for pairing : ")
        pass

    def storingPairs(self):
        for i in range(len(self.string)):
            for j in range(i + 1, len(self.string)):
                self.arr.append(self.string[i] + self.string[j])

    def printList(self):
        for i in range(len(self.arr)):
            print(self.arr[i] + " ", end='')
        print()


str = input("Please input string : ")
obj = StringClass(str)
print(obj.length_of_string())
obj.list_of_character()

obj1 = PairsPossible()
obj1.storingPairs()
obj1.printList()