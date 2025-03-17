# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split()) #for individual values
        index += 1
        numbers = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        if k not in numbers:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
#     test_input = """7
# 5 4
# 1 4 3 4 1
# 4 1
# 2 3 4 4
# 5 6
# 43 5 60 4 2
# 2 5
# 1 5
# 4 1
# 5 3 3 1
# 1 3
# 3
# 5 3
# 3 4 1 5 5

#     """
#     sys.stdin = StringIO(test_input)
    main()