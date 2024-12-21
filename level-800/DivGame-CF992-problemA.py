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
        numbers = list(map(int, data[index].split()))
        index += 1

        found = False
        for i in range(n):
            specificCase = False 
            for j in range(n):
                if i != j and (abs(numbers[i] - numbers[j]) % k) == 0:
                    specificCase = True
                    break
            if not specificCase:
                sys.stdout.write("YES" + "\n" + str(i+1) + "\n")
                found = True
                break

        if not found:
            sys.stdout.write("NO" + "\n")

if __name__ == "__main__":
#     test_input = """7
# 3 2
# 1 2 3
# 4 2
# 1 2 4 5
# 5 3
# 10 7 3 4 5
# 5 3
# 1 31 15 55 36
# 2 1
# 17 17
# 2 2
# 17 18
# 1 3
# 6

#     """
#     sys.stdin = StringIO(test_input)
    main()