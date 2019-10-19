from itertools import combinations_with_replacement

if __name__ == '__main__':
    word, length = input().split()
    print('\n'.join([''.join(pair) for pair in list(combinations_with_replacement(sorted(word), int(length)))]))
