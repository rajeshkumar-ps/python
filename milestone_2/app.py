import utils.database as db
USER_CHOICE  = """
Enter:
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
""" 

def menu():
    user_input = input(USER_CHOICE)
    db.create_book_table()
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            db.list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(USER_CHOICE) 
        pass
    
def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    db.add_book(name, author)      

def prompt_read_book() -> None:
    name = input("Enter the name of the book you have read: ")
    db.mark_book_as_read(name)    

def prompt_delete_book():  
    name = input("Enter the name of the book you want to delete: ")
    db.delete_book(name)  
    
menu()     