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
        array = list(map(int, data[index].split()))
        index += 1

        score = 0
        array.sort()
        i = 0
        while i < n-1:
            if array[i] == array[i+1]:
                score += 1
                i += 2
            else:
                i += 1

        sys.stdout.write(str(score) + "\n")

if __name__ == "__main__":
#     test_input = """5
# 1
# 1
# 2
# 2 2
# 2
# 1 2
# 4
# 1 2 3 1
# 6
# 1 2 3 1 2 3
  
#     """
#     sys.stdin = StringIO(test_input)
    main()