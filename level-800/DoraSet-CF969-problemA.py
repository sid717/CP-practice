# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        l, r = map(int, data[index].split())
        index += 1

        nums = ((r - l) + 1)
        if (nums & 1) and (l & 1) or (r & 1):
            odd = (nums+1) // 2
        else:
            odd = nums // 2

        # result = 0
        # while odd >= 2 and even >= 1:
        #     result += 1
        #     odd -= 2
        #     even -= 1

        sys.stdout.write(str(odd//2) + "\n")


if __name__ == "__main__":
#     test_input = """8
# 1 3
# 3 7
# 10 21
# 2 8
# 51 60
# 2 15
# 10 26
# 1 1000

#     """
#     sys.stdin = StringIO(test_input)
    main()