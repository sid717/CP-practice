from io import StringIO
import sys
import math

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        l, r, k = map(int, data[index].split())
        index += 1
        length = (r-l) + 1
        steps = math.floor(r/k) - l + 1
        maxSteps = max(steps, 0)
            
        sys.stdout.write(str(maxSteps) + "\n")


if __name__ == "__main__":
    test_input = """8
3 9 2
4 9 1
7 9 2
2 10 2
154 220 2
147 294 2
998 24435 3
1 1000000000 2

    """
    sys.stdin = StringIO(test_input)
    main()