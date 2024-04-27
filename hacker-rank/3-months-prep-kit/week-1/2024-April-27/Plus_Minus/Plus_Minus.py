#!/bin/python3
from typing import List
from decimal import Decimal


def plusMinus(arr: List[int]):
    positives = Decimal(0)
    negatives = Decimal(0)
    zeros = Decimal(0)

    if arr:
        total = len(arr)

        for number in arr:
            if number > 0:
                positives += 1
            elif number < 0:
                negatives += 1
            elif number == 0:
                zeros += 1
    percentage_of_positives = round((positives / total), 6)
    percentage_of_negatives = round((negatives / total), 6)
    percentage_of_zeros = round((zeros / total), 6)

    print(
        f"{percentage_of_positives}\n{percentage_of_negatives}\n{percentage_of_zeros}\n"
    )


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
