#!/usr/bin/env python3

ascii_art = {
    'cat':
r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |        hjw | /
  )  |  \  `.___________|/
  `--'   `--'
""",
    'dog': 
r"""
          __
\ ______/ V`-,
}        /~~
/_)^ --,r'
|b      |b
""",
    'fish':
r"""
      /`·.,
     /,...,`:·
 ,.·`  ,   `·.,.·`)
: © ):`;      ,  {
 `·., `·  ,.·`\`·,)
     `\\``\,.·`
"""
}

def main():
    while True:
        choice = input('What animal you like to see?\n').lower()
        if choice in ascii_art.keys():
            print(ascii_art[choice])
            break
        else:
            print('Sorry, that\'s not a valid option!')
            print(f'Valid options are {", ".join(ascii_art.keys())}')

if __name__ == '__main__':
    main()