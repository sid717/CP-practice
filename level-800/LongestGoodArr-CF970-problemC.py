from io import StringIO
import math
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        l, r = map(int, data[index].split())
        index += 1

        nums = r - l + 1

        result = 0
        while l + result <= r:
            l += result
            result += 1

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """5
1 2
1 5
2 2
10 20
1 1000000000

    """
    sys.stdin = StringIO(test_input)
    main()