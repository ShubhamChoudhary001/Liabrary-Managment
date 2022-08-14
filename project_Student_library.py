class Library:
    def __init__(self,listofbooks):
        self.book=listofbooks

    def displayavailablebooks(self):
        print("Books present in this Liabrary are: ")
        for book in self.book:
            print("\t*" +book)
    def borrowbooks(self,bookname):
        if bookname in self.book:
            print(f'You have been issued {bookname}. Kindly keep it safe amd return in 30 days')
            self.book.remove(bookname)
            #return True
        else:
            print("This book is borrowed by somebody check later")  
            #return False  
    def returnbook(self,bookname):
        self.book.append(bookname)        
        print("Thanks for returnimg the book")
class student:
    def requestbook(self):
        self.book=input("Enter the book name you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book


if __name__=="__main__":
    centralLiabrary = Library(["Algorithms","Django","Clrs","python","Think and grow rich","Maths","Physics"])
    student=student()
    #centralLiabrary.displayavailablebooks()
    while(True):
        welcomemsg='''\t***==Welcome to the Central Liabrary==**
                Choose an option:
                1. list all the books
                2. Requeat a Book
                3. Return a Book
                4. Exit Liabrary
        '''
        print(welcomemsg)
        a=int(input("Enter the number of your choice: "))
        if a==1:
            centralLiabrary.displayavailablebooks()
        elif a==2:
            centralLiabrary.borrowbooks( student.requestbook())
        elif a==3:
            centralLiabrary.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing the central library")
            exit()
        else:
            print("invalid Choice")            
        