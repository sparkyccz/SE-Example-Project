idCounter = 0

class Book: 
    def __init__(self, author, title, category):
        global idCounter # global must be in fn "use the global variable that's outside."
        self.__author = author
        self.__title = title
        self.setCategory(category)# this automatically passes "self" in too
        self.__id = idCounter
        idCounter += 1


    # verify that the category is valid
    def setCategory(self, category):
        # non-fiction, fiction, reference
        if category in ["non-fiction", "fiction", "reference"]:
            self.__category = category
        else:
            print("Error: Unknown category")
            self.category = "unknown"

    # display book info
    def display(self):
        # name, author, id, category
        print(f"Title: {self.__title}, Author: {self.__author}, Category: {self.__category}, ID: {self.__id}")

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.___title
    
    def getAuthor(self):
        return self.__author


# TEST
if __name__ == "__main__":
    new_novel = Book(title="Philosopher's Stone", author="J.K. Rowling",category="fiction")
    new_novel.display()