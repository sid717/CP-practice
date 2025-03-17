from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        x = int(data[index])
        index += 1
        
        # found = False
        # if x > 4 or (x & (x - 1)) != 0:
        #     for y in range(x-1, 1, -1):
        #         xor = (x ^ y)
        #         if xor + x > y and xor + y > x and x + y > xor:
        #             result = y
        #             found = True
        #             break

        # if not found:
        #         result = -1

        # if x > 4 and (x & (x - 1)) != 0:
        #     result = (1 << x.bit_length() - 1) - 1
        # else:
        #     result = -1
        if x <= 4:
            result = -1
        elif (x & (x - 1)) == 0:  # x is a power of 2
            result = x - 2
        else:
            result = x - 1

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """7
5
2
6
3
69
4
420

    """
    sys.stdin = StringIO(test_input)
    main()