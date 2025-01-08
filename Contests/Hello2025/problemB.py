# from io import StringIO
import sys
from collections import Counter

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split())
        index += 1
        numbers = list(map(int, data[index].split()))
        index += 1
        
        freq_arr = list(Counter(numbers).values())        
        freq_arr.sort()
        length = len(freq_arr)

        ind = 0

        while ind < length:
            min_val = freq_arr[ind]
            if min_val <= k:
                k -= min_val
                ind += 1
            else:
                break

        result = max(1, length - ind)
        
        sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
#     test_input = """6
# 1 0
# 48843
# 3 1
# 2 3 2
# 5 3
# 1 2 3 4 5
# 7 0
# 4 7 1 3 2 4 1
# 11 4
# 3 2 1 4 4 3 4 2 1 3 3
# 5 5
# 1 2 3 4 5

#     """
#     sys.stdin = StringIO(test_input)
    main()