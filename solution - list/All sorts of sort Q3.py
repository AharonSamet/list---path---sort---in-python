# -*- coding: utf-8 -*-
__author__ = 'Aharon'


def mod3(number):
    return (number % 3) == 0


def sort1(number_list):
    return sorted(number_list, key=lambda number: (number % 3 == 0))

def sort2(number_list):
    number_list.sort(key=mod3)
    number_list.sort()
    return number_list


def sort3(str_list):
    return sorted(str_list, key=lambda str1: (ord(str1[0]) + ord(str1[-1])))



def main():
    """
    Add Documentation here
    """
    print('sort1: \n input = {} output = {}'.format("sort1([9, 3, 2])", sort1([9, 3, 2])))
    print('sort2: \n input = {} output = {}'.format("sort1([9, 3, 2])", sort2([9, 3, 2])))
    print('sort3: \n input = {} output = {}'.format("sort1(['abc', 'aba', 'cba', 'aa'])", sort3(['abc', 'aba', 'cba', 'aa'])))



if __name__ == '__main__':
    main()


    """
    example running:
    sort1:
    input = sort1([9, 3, 2]) output = [2, 9, 3]

    sort2:
    input = sort1([9, 3, 2]) output = [2, 3, 9]

    sort3:
    input = sort1(['abc', 'aba', 'cba', 'aa']) output = ['aba', 'aa', 'abc', 'cba']

Process finished with exit code 0
        """