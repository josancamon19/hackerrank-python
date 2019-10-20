from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    [print(p[0], p[1]) for p in OrderedCounter(sorted(input())).most_common(3)]
    # d = {}
    # for c in s:
    #     d[c] = d.get(c, 0) + 1
