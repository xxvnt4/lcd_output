#!/usr/bin/python3

numbers = [
    " --      --  --      --  --  --  --  -- ",
    "|  |   |   |   ||  ||   |      ||  ||  |",
    "|  |   |   |   ||  ||   |      ||  ||  |",
    "         --  --  --  --  --      --  -- ",
    "|  |   ||      |   |   ||  |   ||  |   |",
    "|  |   ||      |   |   ||  |   ||  |   |",
    " --      --  --      --  --      --  -- "
]

def glyph(number: int, line: int) -> str:
    return ''.join(numbers[line][number*4:number*4+4])

def is_integer():
    global input_string
    input_string = input('> ')
    try:
        int(input_string)
    except:
        print('\nTry again!\n')
        is_integer()

def main():
    print('\nPlease, enter any integer:\n')
    is_integer()

    input_string_len = len(input_string)
    horizontal_line = 'x' + '-' * (4 * input_string_len + input_string_len - 1) + 'x'

    print()
    print('RESULT:\n')
    print(horizontal_line)
    for _ in range(0, 7):
        print('|', end='')
        for symbol in input_string:
            if symbol is input_string[-1]:
                print(glyph(int(symbol), _), end='')
            else:
                print(glyph(int(symbol), _) + ' ', end='')
        print('|')
    print(horizontal_line)
    print()

if __name__ == '__main__':
    main()


