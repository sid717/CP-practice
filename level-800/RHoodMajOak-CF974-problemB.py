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

        # result = "NO"
        # if (k == 1):
        #     if (n % 2 == 0):
        #         result = "YES"
        # elif (k % 2 == 0) and ((k//2) % 2 == 0):
        #         result = "YES"
        # elif (k % 2 != 0) and ((k//2) % 2 == 0):
        #         if (((n-k) + 1) % 2 == 0):
        #             result = "YES"
        # elif (k % 2 != 0) and ((k//2) % 2 != 0):
        #     if (((n-k) + 1) % 2 != 0):
        #             result = "YES"

        if n & 1:
            odd = (k+1) // 2
        else:
            odd = (k) // 2

        sys.stdout.write("NO\n" if odd & 1 else "YES\n")
        
        # sys.stdout.write(result + "\n")

if __name__ == "__main__":
#     test_input = """5
# 1 1
# 2 1
# 2 2
# 3 2
# 4 4

#     """
#     sys.stdin = StringIO(test_input)
    main()