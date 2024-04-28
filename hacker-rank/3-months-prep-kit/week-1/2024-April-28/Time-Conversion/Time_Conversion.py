#!/bin/python3

import os
from typing import AnyStr
from decimal import Decimal


def timeConversion(string: AnyStr):
    hr, min, sec, session = (
        *string.split(":")[:2],
        string.split(":")[2][:2],
        string.split(":")[2][-2:],
    )
    (
        hr,
        min,
        sec,
    ) = (
        Decimal(hr),
        Decimal(min),
        Decimal(sec),
    )

    if session == "PM":
        if hr < 12:
            hr += 12
        return f"{hr:02}:{min:02}:{sec:02}"
    elif session == "AM":
        if hr == 12:
            hr = 0
        return f"{hr:02}:{min:02}:{sec:02}"
    else:
        return f"{hr:02}:{min:02}:{sec:02}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")
    fptr.close()
