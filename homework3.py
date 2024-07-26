import time

def display_menu():
    print('A) Login')
    print('B) Register')
    print('C) Quit')

def handle_login():
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    time.sleep(1)
    print('Attempting to log in...')

def register_menu():
    new_username = input('Enter New Username: ')
    new_password = input('Enter New Password: ')
    print('Account created successfully!')

def menu():
    while True:
        try:
            display_menu()
            choice = input('Select an option (A/B/C): ').upper()
            if choice == "A":
                handle_login()
            elif choice == "B":
                register_menu()
            elif choice == "C":
                print('Exiting program.')
                break
            else:
                print('Invalid choice. Please select A, B, or C.')
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nProgram interrupted. Exiting!')
            break

if __name__ == "__main__":
    menu()
