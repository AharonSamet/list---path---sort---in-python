# -*- coding: utf-8 -*-
__author__ = 'Aharon'


def pathe(s):
    s = s.split('/')
    return ' '.join(s[1:])



def main():
    """
    Add Documentation here
    """
    print(pathe("ww.cyber.org.il/networks/class/ex1"))


if __name__ == '__main__':
    main()