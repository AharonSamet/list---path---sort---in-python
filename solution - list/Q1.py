# -*- coding: utf-8 -*-
__author__ = 'Aharon'


def summer(s):
    if str(s[0]).isdigit():
        return sum(s)
    x = s[0]
    for i in s[1:]:
        x += i
    return x


def main():
    """
    Add Documentation here
    """
    print(summer([1, 2, 4]))
    print(summer(['aa', 'bbb', 'cccc']))
    print(summer([True, True, False, False, True]))

if __name__ == '__main__':
    main()