#!/usr/bin/env python3

ascii_art = {
    'cat': 'CAT ASCII ART HERE',
    'dog': 'DOG ASCII ART HERE',
}

def main():
    choice = input('What animal you like to see?\n').lower()
    if choice in ascii_art.keys():
        print(ascii_art[choice])
    else:
        print('Sorry, that\'s not a valid option!')
        print(f'Valid options are {", ".join(ascii_art.keys())}')

if __name__ == '__main__':
    main()