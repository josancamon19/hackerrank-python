def wrapper(f):
    def fun(l):
        # complete the function
        for i, phone in enumerate(l):
            second = phone[-5:]
            first = phone[-10:-5]
            l[i] = '+91 ' + first + ' ' + second

        f(l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
