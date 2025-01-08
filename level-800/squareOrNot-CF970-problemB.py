# from io import StringIO
import sys
import math

def split_string(s, n, i):
    return [s[j:j+i] for j in range(0, n, i)]

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index]) 
        index += 1
        s = data[index] 
        index += 1

        root = math.sqrt(n)
        result = "YES"
        sum_digits = sum(int(i) for i in str(s))

        if root == int(root) and sum_digits == ((root + (root-2)) * 2):
            root = int(root)
            if '1' not in s[::root] or '1' not in s[n-root:n]:
                result = "NO"
                break
            else:
                parts = split_string(s, n, root)
                for i in range(1, root):
                    if parts[i][0] != '1' or parts[i][root-1] != '1':
                        result = "NO"
                        break
        else:
            result = "NO"

        

        sys.stdout.write(result + "\n")

if __name__ == "__main__":
#     test_input = """5
# 2
# 11
# 4
# 1111
# 9
# 111101111
# 9
# 111111111
# 12
# 111110011111

#     """
#     sys.stdin = StringIO(test_input)
    main()