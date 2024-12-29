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
        a, b = map(int, data[index].split()) 
        index += 1

        # m = min(a,b)
        # n = m
        # math.lcm(a,b)
        # while (m % a) != (m % b):
        #     m += n

        sys.stdout.write(str(math.lcm(a,b)) + "\n")


if __name__ == "__main__":
    test_input = """2
4 6
472 896

    """
    sys.stdin = StringIO(test_input)
    main()