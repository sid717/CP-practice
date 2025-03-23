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
    
        result = 1
        for i in range(2,n+1):
            if n % i == 0:
                result += 1
            else:
                break

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """10
# 2
# 40
# 990990
# 4204474560
# 169958913706572972
# 365988220345828080
# 387701719537826430
# 620196883578129853
# 864802341280805662
# 1000000000000000000

#     """
#     sys.stdin = StringIO(test_input)
    main()