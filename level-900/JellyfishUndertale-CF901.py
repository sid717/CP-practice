# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b, n = map(int, data[index].split())
        index += 1
        numbers = list(map(int, data[index].split()))
        index += 1
        
        result = b-1 if b > 1 else 0
        b = 1

        for i in range(n):
            b = min(a, numbers[i] + 1) - 1
            result += b
        
        sys.stdout.write(str(result + 1) + "\n")


if __name__ == "__main__":
#     test_input = """2
# 5 3 3
# 1 1 7
# 7 1 5
# 1 2 5 6 8

#     """
#     sys.stdin = StringIO(test_input)
    main()