import numpy as np

if __name__ == '__main__':
    n = int(input())
    A = np.array([input().split() for _ in range(n)], int)
    B = np.array([input().split() for _ in range(n)], int)
    print(np.dot(A, B))
