from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    n = int(data[index])
    numbers = []
    index += 1

    for _ in range(n):
        numbers.append(int(data[index]))
        index += 1

    numbers.sort(reverse=True)
    result = numbers[0]


    for i in range(1,n-1):
        result -= numbers[i]
    
    if result == 0 or result == 360


    # sys.stdout.write(result + "\n")


if __name__ == "__main__":
    test_input = """3
10
20
30

    """
    sys.stdin = StringIO(test_input)
    main()