

# create class with attributes
class User:
    def __init__(self, name, library_ID, current_loans=None):
        self.__name = name
        self.__library_ID = library_ID
        self.__current_loans = current_loans if current_loans else[]

    # getter and setter for user
    def get_name(self):
        return self.__name

    def get_library_ID(self):
        return self.__library_ID

    def get_current_loans(self):
        return self.__current_loans
    
    def add_loan(self, book_title):
        self.__current_loans.append(book_title)
    
    def remove_loan(self, book_title):
        self.__current_loans.remove(book_title)

# function for adding user
def add_user(users):
    name = input("Enter user's name: \n").capitalize()
    library_ID = int(input("Enter the user's library ID (e.g., 12-123-12 ): \n").replace('-', ''))
    user = User(name, library_ID)
    users[library_ID] = user
    print(f"User '{name}' added to the library.")

def display_users(users):
    for user in users.values():
        print(f"{user.get_name()} (ID: {user.get_library_ID()}), Current Loans: {user.get_current_loans()}")

def view_user_details(users):
    user_id = int(input("Enter the user's library ID (e.g., 12-123-12 ): \n").replace('-', ''))
    if user_id in users:
        user = users[user_id]
        print(f"Name {user.get_name()}")
        print(f"Library ID: {user.get_library_ID()}")
        print(f"Current Loans: {user.get_current_loans()}")
    else:
        print("User not found.")