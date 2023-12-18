#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_sum = recursive_sum(arr[:mid])
        right_sum = recursive_sum(arr[mid:])
        return left_sum + right_sum


if __name__ == '__main__':
    input_arr = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    print("Сумма элементов массива:", recursive_sum(input_arr))
