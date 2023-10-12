import time
t=time.localtime()
format=time.strftime(f"%d-%m-%y")
class Library:
    def __init__(self,B_list,id):
        self.booklist=B_list
        self.idlist=id

    def showBooks(self):
        print("\n----> List of Available books <----\n")
        for index,item in enumerate (self.booklist):
            print(f"\t{index+1}.{item}\n")
    
    def borrowBook(self,book):
        id=int(input("Please enter your id: "))
        if id in self.idlist:
            if book in self.booklist:
                print(f"'{book}' book has been issued to {id} on date: {format} , Kindly return it within 15 days and keep it safe.")
                self.booklist.remove(book)
        else:
            print("Sorry, Your id is invalid or not registered in the library's system.")

    def returnBook(self,book):
        id=int(input("Please enter your id: "))
        if id in self.idlist:
            print(f"Recieved the '{book}' book from id no - {id} on date: {format}.")
            self.booklist.append(book)
        else:
            print("Sorry, Your id is invalid or not registered in the library's system.")



    def addBook(self,book):
        id=int(input("Please enter your id: "))
        if id in self.idlist:
            self.booklist.append(book)
            print(f"\n'{book}' book is added to the library from id no-{id} on date: {format}, Thank You!")
        else:
            print("Sorry, Your id is invalid or not registered in the library's system.")
        

class Student:
    def __init__(self,name):
        self.name=name
    def borrowBook(self):
        book=input("\nEnter the name of book want to borrow:\n")
        return book
    
    def returnBook(self):
        book=input("\nEnter the name of book want to return:\n")
        return book
    
    def addBook(self):
        book=input("\nEnter the name of book want to add in library:\n")
        return book
        



l1=Library(["c","c++","java","python","dot net","Django","HTTML","CSS","Javascript","React js","Node js","Bootstrap"],
           [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120])

s1=Student("Niko")
if __name__=="__main__":
    while True:
        try:
            print("\t\n****Welcome to IT_World Library****\n")
            print("\nplease select the following number key as per your requirement:\n\n--> Press 1 to access list of books\n--> Press 2 to Borrow Book\n--> Press 3 to return the book\n--> Press 4 to add new books\n--> Press 5 to exit")
            numkey=int(input("\nPlease enter the number key from options:  "))

            if numkey==1:
                l1.showBooks()
            elif numkey==2:
                l1.borrowBook(s1.borrowBook())
            elif numkey==3:
                l1.returnBook(s1.returnBook())
            elif numkey==4:
                l1.addBook(s1.addBook)
            elif numkey==5:
                exit()
        except ValueError:
            print("\nPlease select the valid number key from options.")