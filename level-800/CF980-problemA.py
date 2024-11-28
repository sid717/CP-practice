from io import StringIO
import sys

def profitability(a,b):
    if a >= b:
        balance = a
    else:
        x = (b-a)
        a = a - x
        b = b - (2 * x)
        balance = profitability(a,b)
    return balance

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b = map(int, data[index].split())
        index += 1
        balance = max(profitability(a,b), 0)
        sys.stdout.write(str(balance) + "\n")


if __name__ == "__main__":
    test_input = """5
10 5
7 9
5 100
1 1
1 2

    """
    sys.stdin = StringIO(test_input)
    main()
