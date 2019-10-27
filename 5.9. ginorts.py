if __name__ == '__main__':
    s = input()
    # s = 'Sorting1234'
    s = sorted(s)
    s = sorted(s, key=lambda c: c.isupper())
    s = sorted(s, key=lambda c: c.isdigit())
    s = sorted(s, key=lambda c: c.isdigit() and (c.isdigit() and int(c) % 2 == 0))
    print(''.join(s))
