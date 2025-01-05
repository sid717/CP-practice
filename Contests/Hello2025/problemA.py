# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1

        sys.stdout.write(str(max(n,m) + 1) + "\n")


if __name__ == "__main__":
#     test_input = """3
# 1 1
# 2 2
# 3 5

#     """
#     sys.stdin = StringIO(test_input)
    main()