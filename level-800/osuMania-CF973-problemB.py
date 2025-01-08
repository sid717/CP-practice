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

        for s in reversed(data[index:index + n]):
            sys.stdout.write(str(s.find('#') + 1) + " ")

        index += n

        sys.stdout.write("\n")


if __name__ == "__main__":
#     test_input = """3
# 4
# #...
# .#..
# ..#.
# ...#
# 2
# .#..
# .#..
# 1
# ...#

#     """
#     sys.stdin = StringIO(test_input)
    main()