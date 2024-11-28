from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        s1 = data[index]
        index += 1
        s2 = data[index]
        index += 1

        
        
        sys.stdout.write(str(time) + "\n")


if __name__ == "__main__":
    test_input = """3
GARAGE
GARAGEFORSALE
ABCDE
AABCD
TRAINING
DRAINING

    """
    sys.stdin = StringIO(test_input)
    main()