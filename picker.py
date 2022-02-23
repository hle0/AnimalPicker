#!/usr/bin/env python3

ascii_art = {
    'cat': 'CAT ASCII ART HERE',
    'dog': 'DOG ASCII ART HERE',
}

def main():
    choice = input('What animal you like to see?\n').lower()
    if choice in ascii_art.keys():
        print(ascii_art[choice])

if __name__ == '__main__':
    main()