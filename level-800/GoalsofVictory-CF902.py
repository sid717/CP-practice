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

        print(0 - sum(numbers))

if __name__ == "__main__":
#     test_input = """2
# 4
# 3 -4 5
# 11
# -30 12 -57 7 0 -81 -68 41 -89 0

#     """
#     sys.stdin = StringIO(test_input)
    main()