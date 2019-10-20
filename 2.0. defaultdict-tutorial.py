from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        A.append(input())
    for _ in range(m):
        B.append(input())