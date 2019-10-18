from collections import Counter


def total_earnings(sizes_available, customers):
    counts = Counter(sizes_available)

    # print(sum([price for size, price in customers if size in counts and counts.get(size) > 0]))
    total = 0
    for size, price in customers:
        if size in counts and counts.get(size) > 0:
            total += price
            counts[size] -= 1
    return total


if __name__ == '__main__':
    number_of_shoes = int(input())
    sizes = list(map(int, input().split()))
    customers_pair = []
    for i in range(int(input())):
        customers_pair.append(tuple(map(int, input().split())))
    print(total_earnings(sizes, customers_pair))
