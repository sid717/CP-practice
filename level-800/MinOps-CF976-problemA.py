from io import StringIO
import sys
import math

def power_func(a, b):
    if b == 0:
        return 1
    res = power_func(a, b // 2)
    if b & 1:
        return res * res * a
    else:
        return res * res

def nearest_power(n, k):
    power = int(math.log(n) / math.log(k))
    if power_func(k, (power + 1)) <= n:
        return power + 1
    return power

# def nearest_power(n, k):
#     low, high = 0, n//k
#     while low < high:
#         mid = (low + high + 1) // 2
#         if k ** mid <= n:
#             low = mid
#         else:
#             high = mid - 1
#     return low

def main():
    
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split()) 
        index += 1

        result = 0
        if k > n or k == 1 or n == 1:
            result += n
        else:
            while n >= k:
                n -= power_func(k, nearest_power(n, k))
                result += 1
            result += n

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """6
5 2
3 5
16 4
100 3
6492 10
10 1

    """
    sys.stdin = StringIO(test_input)
    main()