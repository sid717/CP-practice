# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        l, r, d, u = map(int, data[index].split())
        index += 1

        if u == r and r == d and d == l and l == u:
            result = "YES"
        else:
            result = "NO"

        sys.stdout.write(result + "\n")


if __name__ == "__main__":
#     test_input = """2
# 2 2 2 2
# 1 2 3 4

#     """
#     sys.stdin = StringIO(test_input)
    main()