# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        s = data[index]
        index += 1

        sys.stdout.write(str(sum(list(map(int, list(s))))) + "\n")


if __name__ == "__main__":
#     test_input = """5
# 1
# 000
# 1001
# 10101
# 01100101011101

#     """
#     sys.stdin = StringIO(test_input)
    main()