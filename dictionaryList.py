
# List of dictionaries representing books
books = [
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949}
]

# Accessing data from the first dictionary in the list
first_book = books[0]
title_of_first_book = first_book['title']
author_of_first_book = first_book['author']
year_of_first_book = first_book['year']

# Printing the accessed data
print("Title:", title_of_first_book)
print("Author:", author_of_first_book)
print("Year:", year_of_first_book)
