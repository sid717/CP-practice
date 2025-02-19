from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, a, b, c = map(int, data[index].split()) #for individual values
        index += 1

        

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """4
12 1 5 3
6 6 7 4
16 3 4 1
1000000000 1 1 1

    """
    sys.stdin = StringIO(test_input)
    main()