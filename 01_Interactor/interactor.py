import sys


def values_from_file(f):
    try:
        input_file = open(f)
    except FileNotFoundError:
        # print('File not found')
        exit(1)
    values = {}
    values_types = ['exit_code', 'interactor', 'checker']
    cnt = 0
    for line in input_file.readlines():
        try:
            # print(values_types[cnt])
            values[values_types[cnt]] = int(line)
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
    prompts = ['Value r: ', 'Value i: ', 'Value c: ']
    values = {}
    values_types = ['exit_code', 'interactor', 'checker']
    cnt = 0
    for prompt in prompts:
        try:
            values[values_types[cnt]] = int(input())
            cnt += 1
        except ValueError:
            # print('Not integer value passed')
            exit(1)
    return values


def parse_args(a):
    if a['exit_code'] < -128 or a['exit_code'] > 127:
        # print('Bad task finishing code')
        exit(1)
    if a['interactor'] < 0 or a['interactor'] > 7:
        # print('Bad interactor code')
        exit(1)
    if a['checker'] < 0 or a['checker'] > 7:
        # print('Bad checker code')
        exit(1)


def interactor_verdict(a):
    if a['interactor'] == 0 or a['interactor'] == 4:
        if a['exit_code'] != 0:
            return 3
        if a['interactor'] == 4:
            return 4
        else:
            return a['checker']
    if a['interactor'] == 1:
        return a['checker']
    if a['interactor'] == 6:
        return 0
    if a['interactor'] == 7:
        return 1
    return a['interactor']


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
        file.write(str(interactor_verdict(args)))
        file.close()
    else:
        print(interactor_verdict(args))
