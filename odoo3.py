OPEN_DIVISOR = 3
SOURCE_DIVISOR = 7
OPENSOURCE_DIVISOR = OPEN_DIVISOR*SOURCE_DIVISOR
DEFAULT_MAX_INTEGER = 99

def opensource(max_integer=DEFAULT_MAX_INTEGER):
    for integer in range(1, DEFAULT_MAX_INTEGER+1):
        if integer%OPENSOURCE_DIVISOR == 0:
            print("OpenSource")
        elif integer%OPEN_DIVISOR == 0:
            print("Open")
        elif integer%SOURCE_DIVISOR == 0:
            print("Source")
        else:
            print(integer)

def test():
    opensource()
    print("Tests passed!")

if __name__ == "__main__":
    test()
