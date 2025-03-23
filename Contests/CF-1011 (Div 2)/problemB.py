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
        numbers = list(map(int, data[index].split()))
        index += 1

        if 0 not in numbers:
            print(1)
            print(1, n)
        else:
            mid = n//2
            first_zero = numbers[0] == 0
            last_zero = numbers[n-1] == 0
            if first_zero and last_zero:
                print(3)
                print(1, mid)
                print(2, (n-((mid)-1)))
                print(1,2)
            elif first_zero and not last_zero:
                print(2)
                print(1, n-1)
                print(1, 2)
            else:
                print(2)
                print(2, n)
                print(1,2)
                

if __name__ == "__main__":
    test_input = """6
5
0 1 1 1 0
5
0 1 0 0 1
6
0 0 0 0 0 0
6
5 4 3 2 1 0
4
0 0 1 1
4
1 0 0 0

    """
    sys.stdin = StringIO(test_input)
    main()