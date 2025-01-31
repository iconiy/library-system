

def main():
    intro()
    cout = {}
    menu()
    goodbye()

def intro():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~Library Books~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def menu():
    running = True
    while running:
        choice = input('Select an option: '
                       '\n 1. Books'
                       '\n 2. Account'
                       '\n 3. Support'
                       '\n 4. Exit')
        if choice == '1':
            show_books()
            menu()
        if choice == '2':
            account()
            menu()
        if choice == '3':
            support()
            menu()
        if choice == '4':
            running = False

def show_books():
    pass

def account():
    pass

def support():
    print('Please contact our support at support@library.com')

if __name__ == '__main__':
    main()