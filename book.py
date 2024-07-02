#  Book Operations:
#         1. Add a new book
#         2. Borrow a book
#         3. Return a book
#         4. Search for a book
#         5. Display all books
# Book: A class representing individual books with 
# attributes such as title, author,  genre,
#  publication date, and availability status.


# Make a class for Books. Give it attributes.
# main method for this class
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True
         
    # use getters and setters
    def get_title(self):
        return self.__title
    
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_publication_date(self):
        return self.__publication_date

    def get_availability(self):
        return self.__is_available
    
    def set_availability(self):
        if self.get_availability():
            self.__is_available = False
        else:
            self.__is_available = True
    
    def borrow_book(self):
        if self.get_availability():
            self.set_availability()
            return True #returns True are able to borrow
        return False
    
    def return_book(self,):
        self.set_availability()

# Method for adding information for books
def add_book(library):
    title = input("Enter the book's title: \n").capitalize()
    author = input("Enter the book's author: \n").capitalize()        
    genre = input("Enter the book's genre: \n").capitalize()
    publication_date = input("Enter the book's publication_date (YYYY-MM-DD): \n") 
    book = Book(title, author, genre, publication_date)
    library[title] = book
    print(f"Book '{title}' added to the library.")
   
def check_out(library, current_loans):
    title = input("Please enter the book you would like to check out: \n").capitalize()
    user_id = int(input("Please enter library id (e.g., 12-123-12 ): \n").replace('-', '')) 
    if title in library and library[title].borrow_book():
        current_loans[title] = user_id
        # using the getter for the title
        print(f"Book {library[title].get_title()} has been checked out to {user_id}" )
    else:
        print("Book is not available or not found")

def return_book(library, current_loans):
    title = input("Enter the title of the book you would like to return: \n").capitalize()
    user_id = int(input("Please enter library id (e.g., 12-123-12 ): \n").replace('-', ''))
    if title in current_loans and current_loans[title] == user_id:
        library[title].return_book()
        del current_loans[title]
        print(f"Book '{title}' has been successfully returned")
    else:
        print("Invalid return. The book title is incorrect or user Id does not match")

def search_book(library):
    title = input("What is the title you're looking for? \n").capitalize()
    if title in library:
        book = library[title]
        print("Book found, here is some info: \n")
        print(book.get_title())
        print(book.get_author())
        print(book.get_genre())
        print(book.get_publication_date())
        print(book.get_availability())
    else:
        print("Sorry! That book is not in our library.")
      
def display_books(library):
    for book in library.values():
        print(f"{book.get_title()} by {book.get_author()} - Genre: {book.get_genre()} - Available: {'Yes' if book.get_availability() else 'No'}")

        
     

 