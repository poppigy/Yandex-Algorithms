import sys


def values_from_file(f):
    try:
        input_file = open(f)
    except FileNotFoundError:
        # print('File not found')
        exit(1)
    values = {}
    values_types = ['first', 'second', 'year']
    cnt = 0
    input_values = input_file.read().split(' ')
    if len(input_values) != 3:
        exit(1)
    for v in input_values:
        try:
            # print(values_types[cnt])
            values[values_types[cnt]] = int(v)
            # print(values[values_types[cnt]], ':', cnt)
            cnt += 1
        except ValueError:
            # print('Not integer value passed')
            exit(1)
    input_file.close()
    if cnt != 3:
        # print('Input data is invalid')
        exit(1)
    return values


def values_from_input():
    values = {}
    values_types = ['first', 'second', 'year']
    cnt = 0
    input_values = input().split(' ')
    if len(input_values) != 3:
        exit(1)
    for value_type in values_types:
        try:
            values[value_type] = int(input_values[cnt])
            cnt += 1
        except ValueError:
            # print('Not integer value passed')
            exit(1)
    return values


def parse_args(a):
    if a['first'] < 1 or a['first'] > 31:
        # print('Bad task finishing code')
        exit(1)
    if a['second'] < 1 or a['second'] > 31:
        # print('Bad interactor code')
        exit(1)
    if a['year'] < 1970 or a['year'] > 2069:
        # print('Bad checker code')
        exit(1)


def station_cnt(a):
    if a['first'] < 13 and a['second'] < 13:
        if a['first'] == a['second']:
            return 1
        return 0
    return 1


if __name__ == '__main__':
    args = {}
    # print(len(sys.argv))
    if len(sys.argv) == 2:
        if sys.argv[1] == "input.txt":
            args = values_from_file(sys.argv[1])
        else:
            # print("Bad file name: input.txt expected")
            exit(1)
    elif len(sys.argv) == 1:
        args = values_from_input()
    else:
        # print('Input data is invalid')
        exit(1)
    parse_args(args)
    if len(sys.argv) == 2:
        file = open('output.txt', "w")
        file.write(str(station_cnt(args)))
        file.close()
    else:
        print(station_cnt(args))
