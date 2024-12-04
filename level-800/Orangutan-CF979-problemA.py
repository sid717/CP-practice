from io import StringIO
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
        array = list(map(int, data[index].split()))
        index += 1

        score = 0
        array.sort()
        
        sys.stdout.write(str(score) + "\n")

if __name__ == "__main__":
    test_input = """3
1
69
3
7 6 5
5
1 1 1 2 2

    """
    sys.stdin = StringIO(test_input)
    main()