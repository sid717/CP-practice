# from io import StringIO
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
        a = list(map(int, data[index].split()))
        index += 1
        b = list(map(int, data[index].split()))
        index += 1

        result = a[n-1]
        for i in range(n-1):
            result += max(0, (a[i] - b[i+1]))

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 2
# 3 2
# 2 1
# 1
# 5
# 8
# 3
# 1 1 1
# 2 2 2
# 6
# 8 2 5 6 2 6
# 8 2 7 4 3 4

#     """
#     sys.stdin = StringIO(test_input)
    main()