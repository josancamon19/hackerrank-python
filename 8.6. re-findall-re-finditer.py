import re

if __name__ == '__main__':
    s = '[qwrtypsdfghjklzxcvbnm]'
    a = re.findall('(?<=' + s + ')([aeiou]{2,})' + s, input(), re.I)
    print('\n'.join(a or ['-1']))
