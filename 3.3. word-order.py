if __name__ == '__main__':
    words = [input() for _ in range(int(input()))]
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1

    print(len(set(words)))
    print(' '.join([str(value) for key, value in words_dict.items()]))

