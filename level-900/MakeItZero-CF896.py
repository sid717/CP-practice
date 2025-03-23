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
        numbers = list(map(int, data[index].split()))
        index += 1

        if n & 1 == 1:
            print(4)
            print(1, 2)
            print(1, 2)
            print(2, n)
            print(2, n)
        else:
            print(2)
            print(1, n)
            print(1, n)
            
if __name__ == "__main__":
#     test_input = """6
# 4
# 1 2 3 0
# 8
# 3 1 4 1 5 9 2 6
# 6
# 1 5 4 1 4 7
# 5
# 0 0 0 0 0
# 7
# 1 1 9 9 0 1 8
# 3
# 100 100 0

#     """
#     sys.stdin = StringIO(test_input)
    main()