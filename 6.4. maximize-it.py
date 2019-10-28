from itertools import product

f = lambda x: x ** 2

f_list = lambda l, mod: sum([f(n) for n in l]) % mod

if __name__ == '__main__':
    K, M = tuple(map(int, input().split()))
    s = [list(map(int, input().split()[1:])) for _ in range(K)]
    print(max([f_list(p, M) for p in product(*s)]))
