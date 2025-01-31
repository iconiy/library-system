
class Book:

    def __init__(self, title, author, year, genre, isbn, rental_length):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.rental_length = rental_length

    def check_out(self):
        rental_length = 14
        print(f'You are about to check out {self.title} by {self.author} for {rental_length} days.')
        choice = input('Press Enter to check out...')
        if choice == '':
            print(f'You have successfully checked out {self.title} by {self.author}.')
        else:
            print('Cancelled transaction.')

    def get_info(self):
        print(f'Title: {self.title}'
              f'\nAuthor: {self.author}'
              f'\nYear: {self.year}'
              f'\nGenre: {self.genre}')