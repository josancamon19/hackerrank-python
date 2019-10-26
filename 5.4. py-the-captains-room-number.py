if __name__ == '__main__':
    k = int(input())
    d = dict()
    for t in list(map(int, input().split())):
        if d[t] == k:
            del d[t]
        else:
            d[t] = d.get(t, 0) + 1

    for k in d.keys():
        print(k)
