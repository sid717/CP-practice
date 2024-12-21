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
        array = list(map(int, data[index].split()))
        index += 1
        result, total, new_k = 0, sum(array), k

        if total < k:
            result += (k-total)
        elif total > k:
            array.sort(reverse=True)
            for i in range(n+1):
                if new_k == 0:
                    break
                elif new_k < 0:
                    result = k - sum(array[:i-1])
                    break
                new_k -= array[i]


        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 5 4
# 4 1 2 3 2
# 5 10
# 4 1 2 3 2
# 2 10
# 1 1
# 3 8
# 3 3 3

#     """
#     sys.stdin = StringIO(test_input)
    main()