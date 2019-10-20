from itertools import groupby

if __name__ == '__main__':
    print(' '.join([str((len(list(map(int, v))), int(k))) for k, v in groupby(input())]))
