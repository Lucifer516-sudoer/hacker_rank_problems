#!/bin/python3
from typing import List


def miniMaxSum(arr: List[int]):
    smallest_number = min(arr)
    largest_number = max(arr)

    min_sum = sum(arr) - largest_number
    max_sum = sum(arr) - smallest_number

    print(min_sum, max_sum)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
