# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        steps = 1
        while (n > 3):
            n //= 4
            steps *= 2

        sys.stdout.write(str(steps) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 1
# 5
# 16
# 1000000000000000000

#     """
#     sys.stdin = StringIO(test_input)
    main()