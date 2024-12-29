# from io import StringIO
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

        if x % 33 == 0:
            result = "YES"
        else:
            result = "NO"

        sys.stdout.write(result + "\n")


if __name__ == "__main__":
#     test_input = """5
# 165
# 6369
# 666
# 114514
# 133333332

#     """
#     sys.stdin = StringIO(test_input)
    main()