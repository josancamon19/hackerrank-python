if __name__ == '__main__':
    input()
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        ct = input().split()  # command, target
        if len(ct) > 1:
            eval('s.' + ct[0] + '(' + str(ct[1]) + ')')
        else:
            eval('s.' + ct[0] + '()')

    print(sum(s))
