#!/bin/python3
import os
from typing import List


# Complete the 'breakingRecords' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
def breakingRecords(scores: List[int]) -> List[int]:
    # Initialize min_rec and max_rec with the first score
    min_rec, max_rec = scores[0], scores[0]
    min_count, max_count = 0, 0

    for score in scores:
        if score < min_rec:
            min_rec = score
            min_count += 1
        elif score > max_rec:
            max_rec = score
            max_count += 1

    return [max_count, min_count]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
