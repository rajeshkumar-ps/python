"""
concerned about storing and retrieving from book list
"""

books_file = 'books.txt'

def create_book_table():
    with open(books_file, 'w') as f:
        pass

def add_book(name, author):
    with open(books_file, 'a') as f:
        f.write(f'{name},{author},0\n')
        print(f'Book "{name}" by {author} added.')  
        
def list_books():  
    with open(books_file, 'r') as f:  
        lines = [line .strip().split(',') for line in f.readlines()]
        return [{'name': line[0], 'author': line[1], 'read': line[2] == '1'} for line in lines]
        
def mark_book_as_read(name):
    print('coming')
    books = list_books()
    print(books)
    for book in books:
        if book['name'].lower() == name.lower():
            book['read'] = '1'
            print(f'Book "{name}" marked as read.')
        _save_books(books)    
        
def _save_books(books):  
    with open(books_file, 'w') as f:
        for book in books:
            read_flag = '1' if book['read'] else '0'
            f.write(f"{book['name']},{book['author']},{read_flag}\n")          

def delete_book(name):
    books = list_books()
    books = [book for book in books if book['name'].lower() != name.lower()]
    _save_books(books)
