if __name__ == '__main__':
    _, english, _, french = input(), set(input().split()), input(), set(input().split())
    print(len(english.union(french)))
