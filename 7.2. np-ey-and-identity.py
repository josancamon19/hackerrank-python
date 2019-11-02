import numpy as np

if __name__ == '__main__':
    N, M = tuple(map(int, input().split()))
    print(np.eye(N, M))
