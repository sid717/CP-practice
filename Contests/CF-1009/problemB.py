# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index]) #for individual value
        index += 1
        numbers = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        print(sum(numbers)-(n-1))

if __name__ == "__main__":
#     test_input = """4
# 1
# 10
# 3
# 998 244 353
# 5
# 1 2 3 4 5
# 9
# 9 9 8 2 4 4 3 5 3

#     """
#     sys.stdin = StringIO(test_input)
    main()