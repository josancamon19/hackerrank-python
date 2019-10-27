if __name__ == '__main__':
    _, n = input(), input().split()
    print(all([int(i) > 0 for i in n]) and any(i == i[::-1] for i in n))
