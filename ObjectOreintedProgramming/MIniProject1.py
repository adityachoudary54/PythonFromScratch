"""
Create a library class
- displayBook
- lend Book
- add Book
- return Book
objectName=Library(listOfBooks,libraryName)
"""
# can be done
"""
maintain a dict to associate a book with whom its issued
dict-{book,nameOfPerson}
"""

class Library():
    def __init__(self,listOfBooks,libraryName):
        # super().__init__()
        self.listOfBooks=set(listOfBooks)
        self.libraryName=libraryName
        self.listOfBooksInLib=set(listOfBooks)
    def displayBook(self):
        return f"The books offered by library are {self.libraryName} are :{self.listOfBooks}.\nThe books currently present in library are   {self.libraryName} are :{self.listOfBooksInLib}."
    def addBook(self,*args):
        for item in args:
            self.listOfBooks.add(item)
            self.listOfBooksInLib.add(item)
    def returnBook(self,book):
        if book in self.listOfBooks:
            self.listOfBooksInLib.add(book)
        else:
            print("This book doesn't belongs to library")
    def lendBook(self,book):
        if book in self.listOfBooksInLib:
            self.listOfBooksInLib.remove(book)
        else:
            print("The given book can't be lended.")

print("Welcome to library system management")
adiLibrary=Library([],'Adi Library')
while True:
    print("Enter your choice(1/2/3/4)->")
    print('1 ->displayBook')
    print('2 ->lend Book')
    print('3 ->add Book')
    print('4 ->return Book')
    ch=int(input())
    if ch==1:
        print(adiLibrary.displayBook())
    elif ch==2:
        print(adiLibrary.displayBook())
        book=input("Enter the book u req:")
        adiLibrary.lendBook(book)
    elif ch==3:
        books=input("Enter the books u want to add:").split(",")
        adiLibrary.addBook(*books)
    elif ch==4:
        book=input("Enter the books u want to return:")
        adiLibrary.returnBook(book)
    else:
        print("Bye come again next time")
        break

