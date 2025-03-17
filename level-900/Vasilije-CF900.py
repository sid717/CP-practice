# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k, x = map(int, data[index].split())
        index += 1

        series_n = (n * (n+1) // 2)
        series_k = (k * (k+1) // 2)
        digits = n - k
        series_sub = (digits * (digits+1) // 2)

        if series_k > series_n:
            print("NO")
        elif k >= x and k > 1:
            print("NO")
        elif series_n - series_sub < x:
            print("NO")
        elif x >= series_k and x <= series_n:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
#     test_input = """12
# 5 3 10
# 5 3 3
# 10 10 55
# 6 5 20
# 2 1 26
# 187856 87856 2609202300
# 200000 190000 19000000000
# 28 5 2004
# 2 2 2006
# 9 6 40
# 47202 32455 613407217
# 185977 145541 15770805980

#     """
#     sys.stdin = StringIO(test_input)
    main()