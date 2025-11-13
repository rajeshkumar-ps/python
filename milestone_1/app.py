# As a user I would like to be able to add new movie to my collection
# Add new movie to my collection
# List All The Movie in my collection
# Find Movie by title
MENU_PROMPT = "\n Enter 'a' to add movie,'l' to see your movies, 'f' to find a movie by title , or 'q' to quit"
movies = []
def add_movies(movie):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    year = input("Enter year: ")
    movies.append({"title": title, "director": director, "year": year})

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title :{movie["title"]}")
    print(f"director: {movie["director"]}")
    print(f" movie :{movie["year"]}")

def find_movie():
    search_title = input("Enter movie title to search: ")
    for movie in movies:
        if movie["title"].lower() == search_title.lower():
            print_movie(movie)

user_options = {
    "a": add_movies,
    "l": show_movies,
    "f": find_movie
}    

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            user_options[selection]()
        else:
            print("Unknown command. Please try again.")
        selection = input(MENU_PROMPT)        
        
menu()        