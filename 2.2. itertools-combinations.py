from itertools import combinations

get_combinations = lambda word, length: '\n'.join(
    [''.join(pair) for i in range(1, length + 1) for pair in combinations(sorted(word), i)]
)

if __name__ == '__main__':
    # w, l = input().split()
    # print_combinations(w, int(l))
    print(get_combinations('HACK', 2))
