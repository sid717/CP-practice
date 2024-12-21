# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        newIndex = index
        result = 0
        for _ in range(n):
            s = data[newIndex]
            m -= len(s)
            if m < 0:
                break
            elif m == 0:
                result += 1
                break
            else:
                result += 1
            newIndex += 1

        index += n
        
        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """5
# 3 1
# a
# b
# c
# 2 9
# alpha
# beta
# 4 12
# hello
# world
# and
# codeforces
# 3 2
# ab
# c
# d
# 3 2
# abc
# ab
# a

#     """
#     sys.stdin = StringIO(test_input)
    main()