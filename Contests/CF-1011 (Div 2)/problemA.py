# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split())
        index += 1
        s = data[index]
        index += 1

        if n == 1:
            print("NO")
        elif len(set(s)) > 1 and k >= 1:
            print("YES")
        elif ord(s[0]) < ord(s[n-1]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
#     test_input = """8
# 1 10000
# a
# 3 3
# rev
# 6 0
# string
# 6 0
# theory
# 9 2
# universal
# 19 0
# codeforcesecrofedoc
# 19 1
# codeforcesecrofedoc
# 3 1
# zzz

#     """
#     sys.stdin = StringIO(test_input)
    main()