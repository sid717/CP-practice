# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b = map(int, data[index].split())
        index += 1

        sys.stdout.write(str(((a-a) + (b-a))) + "\n")


if __name__ == "__main__":
#     test_input = """3
# 1 2
# 3 10
# 5 5

#     """
#     sys.stdin = StringIO(test_input)
    main()