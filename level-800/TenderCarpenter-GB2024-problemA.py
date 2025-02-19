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

        found = False

        for i in range(n-1):
            if numbers[i] * 2 <= numbers[i+1] or numbers[i+1] * 2 <= numbers[i]:
                continue
            else:
                found = True
                break

        if found:
            sys.stdout.write("YES" + "\n")
        else:
            sys.stdout.write("NO" + "\n")


if __name__ == "__main__":
#     test_input = """5
# 4
# 2 3 5 7
# 4
# 115 9 2 28
# 5
# 8 4 1 6 2
# 6
# 1 5 4 1 4 7
# 2
# 100000 100000

#     """
#     sys.stdin = StringIO(test_input)
    main()