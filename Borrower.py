borrowerIdCounter = 0

class Borrower:
    def __init__(self, name, role):
        self.__name = name
        global borrowerIdCounter
        self.__id = borrowerIdCounter
        borrowerIdCounter += 1
        self.setRole(role)

    def setRole(self, role):
        if role in ["staff", "student", "parent"]:
            self.__role = role
        else:
            print("Error: Invalid role.")
            self.__role = "unknown"

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Role: {self.__role}")
        print(f"ID: {self.__id}")

    def getName(self):
        return self.__name
    def getID(self):
        return self.__id
    def getRole(self):
        return self.__role

if __name__ == "__main__":
    myBorrower = Borrower("Angus", "staff")
    myBorrower.display()