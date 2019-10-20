from collections import deque

if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        ct = input().split()  # command, target
        if len(ct) > 1:
            eval('d.' + ct[0] + '(' + str(ct[1]) + ')')
        else:
            eval('d.' + ct[0] + '()')

    print(*d)
