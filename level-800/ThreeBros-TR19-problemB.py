# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    a, b = map(int, data[index].split())

    sys.stdout.write(str(6 - (a + b)) + "\n")


if __name__ == "__main__":
    # test_input = """3 1

    # """
    # sys.stdin = StringIO(test_input)
    main()