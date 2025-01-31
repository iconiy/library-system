import sys
import book as b

def main():
    intro()
    hp = b.Book('Harry Potter', 'JP', '2000', 'Fantasy', '234', 14)
    menu(hp)
    goodbye()

def intro():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~Library Books~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def menu(hp):
    running = True
    while running:
        print('1. Books'
             '\n2. Account'
             '\n3. Support'
             '\n4. Exit')
        choice = input('Select an option: ')
        if choice == '1':
            show_books()
            menu()
        if choice == '2':
            account(hp)
            menu(hp)
        if choice == '3':
            support()
            menu()
        if choice == '4':
            sys.exit(0)

def show_books():
    pass

def account(hp):
    b.Book.get_info(hp)

def support():
    print('Please contact our support at support@library.com')



if __name__ == '__main__':
    main()