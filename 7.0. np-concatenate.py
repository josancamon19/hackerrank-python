import numpy as np

if __name__ == '__main__':
    N, M, P = tuple(map(int, input().split()))
    print(np.array([np.array(input().split(), int) for _ in range(N + M)]))
