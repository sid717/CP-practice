# from io import StringIO
import sys
# import math

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k, p = map(int, data[index].split()) #for individual values
        index += 1

        result = 0
        sums = 0
        k = abs(k)
        if n * p < k:
            result = -1
        else:
            for _ in range(n):
                if sums >= k:
                    break
                sums += p
                result += 1
        
        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """8
# 21 100 10
# 9 -420 42
# 5 -7 2
# 13 37 7
# 10 0 49
# 1 10 9
# 7 -7 7
# 20 31 1

#     """
#     sys.stdin = StringIO(test_input)
    main()