from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, x = map(int, data[index].split()) #for individual values
        index += 1



        for _ in range(n):
            sys.stdout.write(str(result) + " ")

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """9
1 69
7 7
5 7
7 3
8 7
3 52
9 11
6 15
2 3

    """
    sys.stdin = StringIO(test_input)
    main()