from collections import OrderedDict

if __name__ == '__main__':
    ordered_dict = OrderedDict()
    for i in range(int(input())):
        pair = input()
        key = pair[:pair.rfind(' ') + 1].strip()
        value = pair[pair.rfind(' '):]
        if key in ordered_dict:
            ordered_dict[key].append(int(value))
        else:
            ordered_dict[key] = [int(value)]

    for key, value in ordered_dict.items():
        print(key, sum(value))
        # print(key.strip() + ': Quantity bought:', str(len(value)) + ', Price:', value[0])
        # print('Net Price:', sum(value))
