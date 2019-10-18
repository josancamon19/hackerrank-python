from itertools import product

cartesian_product = lambda x_list, y_list: print(*product(x_list, y_list))

if __name__ == '__main__':
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    cartesian_product(X, Y)
