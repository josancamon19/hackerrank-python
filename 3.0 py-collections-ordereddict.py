from collections import OrderedDict

if __name__ == '__main__':
    ordered_dict = OrderedDict()
    for i in range(int(input())):
        key, value = input().rsplit(' ', 1)
        ordered_dict[key] = ordered_dict.get(key, 0) + int(value)

    for key, value in ordered_dict.items():
        print(key, value)
