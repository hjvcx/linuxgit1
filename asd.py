from docopt import docopt

usage = '''
Usage:
asd.py -a
asd.py -s
asd.py -d
'''

if __name__ == '__main__':
    args = docopt(usage)

    if args['-a']:
        print('Aboba')

    if args['-s']:
        print('Spaghetti')

    if args['-d']:
        print('Drained')



