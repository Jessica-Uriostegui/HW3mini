# Jessica Uriostegui
# July 1, 2024

# Module 4: Mini-Project | Library Management System

# import files
import book
import user
import author


# create main method (driver file)
def main(): 
    # dictionary that will store the key ,value will be book
    library = {} 
    current_loans = {}
    authors = {}
    users = {} 
    
    while True:
        # greeting with menu with options
        print("""
        
              Welcome what would you like to do: 
              
        1. Add Book
        2. Checkout A Book
        3. Search A Book
        4. Display All Books
        5. Add Author with Biography
        6. View Author details
        7. Display All Authors
        8. Add User
        9. View User Details
        10. Display All Users
        11. Return A Book
        12. Exit
        """)
        print("******************************************** \n")
        
        choice = input("Enter your choice: \n")
        
        try:
            if choice == "1":
                book.add_book(library)
            elif choice == "2":
                book.check_out(library, current_loans)
            elif choice == "3":
                book.search_book(library)
            elif choice == "4":
                book.display_books(library)
            elif choice == "5":
                author.add_author(authors)
            elif choice == "6":
                author_name = input("Enter tha author's name: \n").capitalize()
                if author_name in authors:
                    print(f"Name: {authors[author_name].get_name()}")
                    print(f"Biography: {authors[author_name].get_biography()}")
                else:
                    print("Author not found. ")
            elif choice == "7":
                author.display_authors(authors)
            elif choice == "8":
                user.add_user(users)
            elif choice == "9":
                user.view_user_details(users)
            elif choice == "10":
                user.display_users(users)
            elif choice == "11":
                book.return_book(library, current_loans)
            elif choice == "12":
                print("Thank you have a great day. Good bye.")
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print(f"An error occurred: {e}")
main()

