from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b = map(int, data[index].split()) #for individual values
        n = int(data[index]) #for individual value
        numbers = list(map(int, data[index].split())) #for inputting into an array
        s = data[index] #for inputting into a string
        index += 1

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """
    """
    sys.stdin = StringIO(test_input)
    main()