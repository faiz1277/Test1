import filecmp


if __name__ == "__main__":
    loc1 = "test.txt"
    loc2 = "test2.txt"

    compare = filecmp.cmp(loc1, loc2)

    print(compare)

    if compare:
        print("Files are identical")
    else:
        print("Files are different")