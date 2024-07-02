

# made a class for Authors and made methods 
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        
    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography

# add author information   
def add_author(authors):
    name = input("Enter the author's name: \n").capitalize()
    biography = input("Enter the author's biography: \n").capitalize()
    author = Author(name, biography)
    authors[name] = author
    print(f"Author '{name}' added to the library.")

def display_authors(authors):
    for author in authors.values():
        print(f"{author.get_name()}: {author.get_biography()}")
    
    

           