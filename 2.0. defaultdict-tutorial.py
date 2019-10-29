if __name__ == '__main__':
    n, m = map(int, input().split())
    A = [input() for _ in range(n)]
    B = [input() for _ in range(m)]

    [print(' '.join([str(i + 1) for i, w in enumerate(A) if w == word])) if word in A else print(-1) for word in B]

    # for word in B:
    #     if word not in A:
    #         print(-1)
    #     else:
    #         print(' '.join([str(i + 1) for i, w in enumerate(A) if w == word]))

    # for word in B:
    #     if word not in A:
    #         print(-1)
    #     else:
    #         w_idx_a = []
    #         for i, w in enumerate(A):
    #             if w == word:
    #                 w_idx_a.append(i + 1)
    #
    #             if i == len(A) - 1:
    #                 print(' '.join(list(map(str, w_idx_a))))
