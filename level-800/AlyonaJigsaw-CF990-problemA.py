# from io import StringIO
import sys
import math

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        array = list(map(int, data[index].split()))
        index += 1
        blocks, layers = 0, 0
        for i in range(n):
            blocks += array[i]
            sqrt = math.sqrt(blocks)
            if sqrt == int(sqrt) and int(sqrt) % 2 != 0:
                layers += 1

        sys.stdout.write(str(layers) + "\n")


if __name__ == "__main__":
#     test_input = """5
# 1
# 1
# 2
# 1 8
# 5
# 1 3 2 1 2
# 7
# 1 2 1 10 2 7 2
# 14
# 1 10 10 100 1 1 10 1 10 2 10 2 10 1

#     """
#     sys.stdin = StringIO(test_input)
    main()