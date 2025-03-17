from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b, n = map(int, data[index].split()) #for individual values
        index += 1
        numbers = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        result = 0
        for i in range(n):
            if numbers[i] + b >= a:
                result += 1

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """2
5 3 3
1 1 7
7 1 5
1 2 5 6 8

    """
    sys.stdin = StringIO(test_input)
    main()