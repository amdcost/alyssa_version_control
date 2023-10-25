# Version Control Lab 06!
def password_encoder(encode):
    # only integers allowed, each digit shifted up by 3
    # ie 1234555 = 4567888

    password = ''
    for i in encode:
        formula = str((int(i) + 3) % 10)
        password += formula
    return password

def decoder(input1): ## alex
    output = ""
    for digit in input1:
        x = str((int(digit) - 3) % 10)
        output += x

    return output

def menu():
    res = ''
    res2 = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        option = input('Please enter an option: ')
        if option == '1':
            encode = (input('Please enter your password to encode: '))
            res = password_encoder(encode)
            print('Your password has been encoded and stored!')
            # Partner to help with else section
        elif option == '2':
            res2 = decoder(res)
            print(f"The encoded password is {res}, and the original password is {res2}.")
        elif option == '3':
            break
            
            


if __name__ == '__main__':
    menu()
