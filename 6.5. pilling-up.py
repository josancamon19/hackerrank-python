if __name__ == '__main__':
    for _ in range(int(input())):
        n_len, n = int(input()), list(map(int, input().split()))
        stack = []
        i = 0
        while i < n_len:
            f = n[0]
            l = n[-1]

            if len(stack) > 0 and max([f, l]) > stack[-1]:
                break

            if f > l:
                stack.append(f)
                del n[0]
            else:
                stack.append(l)
                del n[-1]

            i += 1

        print('Yes' if len(stack) == n_len else 'No')
