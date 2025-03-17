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
        x = data[index] 
        index += 1
        s = data[index]
        index += 1

        for i in range(6):
            if s in x:
                print(i)
                break
            x += x
        if s not in x:
            print(-1)

        
if __name__ == "__main__":
#     test_input = """12
# 1 5
# a
# aaaaa
# 5 5
# eforc
# force
# 2 5
# ab
# ababa
# 3 5
# aba
# ababa
# 4 3
# babb
# bbb
# 5 1
# aaaaa
# a
# 4 2
# aabb
# ba
# 2 8
# bk
# kbkbkbkb
# 12 2
# fjdgmujlcont
# tf
# 2 2
# aa
# aa
# 3 5
# abb
# babba
# 1 19
# m
# mmmmmmmmmmmmmmmmmmm

#     """
#     sys.stdin = StringIO(test_input)
    main()