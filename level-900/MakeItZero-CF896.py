from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index]) #for individual value
        index += 1
        numbers = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """
    """
    sys.stdin = StringIO(test_input)
    main()