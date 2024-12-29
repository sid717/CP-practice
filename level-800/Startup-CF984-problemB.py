# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1
    
    for _ in range(t):
        n, k = map(int, data[index].split())
        index += 1
        cost = [0] * k
        
        for _ in range(k):
            b_i, c_i = map(int, data[index].split())
            cost[(b_i - 1)] += c_i
            index += 1

        cost.sort(reverse = True)

        sys.stdout.write(str(sum(cost[:n])) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 3 3
# 2 6
# 2 7
# 1 15
# 1 3
# 2 6
# 2 7
# 1 15
# 6 2
# 1 7
# 2 5
# 190000 1
# 1 1000

#     """
#     sys.stdin = StringIO(test_input)
    main()