import filecmp
import pandas as pd
import numpy

if __name__ == "__main__":
    loc1 = "test.txt"
    loc2 = "test2.txt"

    compare = filecmp.cmp(loc1, loc2)

    print(compare)

    if compare:
        print("Files are identical")
    else:
        print("hey")