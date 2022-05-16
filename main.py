import string
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    again = ''

    while again != 'no':
        option = input('Enter \'encode\' to encrypt, \'decode\' to decrypt: ')
        if option not in ['encode', 'decode']:
            print('invalid option: please choose encode or decode')
            clear()
            continue
        
        message = input('Enter a message: ').lower()
        shift = int(input('Enter a shift number: '))
        result = cipher(
            message, shift) if option == 'encode' else cipher(
            message, -shift)

        print(f'\nHere\'s the result: {result}')
        again = input('\nType \'yes\' to go again, \'no\' to exit: ')
        clear()


def cipher(message, shift):
    letters = list(string.ascii_lowercase)
    cipher_letters = letters[shift:] + letters[:shift]
    scheme = {
        letters[index]: cipher_letters[index] for index in range(len(letters))
    }

    return ''.join([scheme[ch] for ch in message])


if __name__ == '__main__':
    main()
