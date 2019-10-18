# def print_formatted(number):
#     values = []
#     prev_value = []
#
#     for i in reversed(range(1, number + 1)):
#         oct_v = oct(i).replace('0o', '')
#         hex_v = hex(i).replace('0x', '').capitalize()
#         bin_v = bin(i).replace('0b', '')
#
#         if len(values) > 0:
#             i = ' ' * (len(prev_value[0]) - len(str(i))) + str(i)
#             oct_v = ' ' * (len(prev_value[1]) - len(oct_v)) + oct_v
#             hex_v = ' ' * (len(prev_value[2]) - len(hex_v)) + hex_v
#             bin_v = ' ' * (len(prev_value[3]) - len(bin_v)) + bin_v
#         else:
#             i = ' ' + str(i)
#             oct_v = '  ' + oct_v
#             hex_v = '  ' + hex_v
#             bin_v = ' ' + bin_v
#
#         value = [str(i), str(oct_v), str(hex_v), str(bin_v)]
#         prev_value = value
#
#         values.append(value)
#
#     for value in reversed(values):
#         print(''.join(value))


def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        # print('{0:4b}'.format(i))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    # n = int(input())
    print_formatted(12)
