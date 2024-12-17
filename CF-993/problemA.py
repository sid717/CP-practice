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


        sys.stdout.write(str(n-1) + "\n")


if __name__ == "__main__":
#     test_input = """3
# 2
# 4
# 6

#     """
#     sys.stdin = StringIO(test_input)
    main()