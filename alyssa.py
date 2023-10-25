# Version Control Lab 06!
def password_encoder(encode):
    # only integers allowed, each digit shifted up by 3
    # ie 1234555 = 4567888

    password = ''
    for i in encode:
        formula = str((int(i) + 3) % 10)
        password += formula
    return password


def menu():
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3 Quit')
    option = input('Please enter an option: ')
    res = ''
    while option != '3':
        if option == '1':
            encode = (input('Please enter your password to encode: '))
            res = password_encoder(encode)
            print('Your password has been encoded and stored!')
        # Partner to help with else section
        elif option == '2':
            pass


if __name__ == '__main__':
    menu()
