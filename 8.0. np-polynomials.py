if __name__ == '__main__':
    print(__import__('numpy').polyval(list(map(float, input().split())), float(input())))
