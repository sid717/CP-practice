from io import StringIO
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

        # solution 1:

        mods = [i for i in range(n)]
        result = [2]

        for i in range(1, n):
            maxValue = max(result)
            for j in range(maxValue+1, 100):
                if j % (i+1) == mods[i]:
                    result.append(j)
                    break
        
        for i in range(n):
            sys.stdout.write(str(result[i]) + " ")
        sys.stdout.write("\n")

        # solution 2:
        for i in range(1, n+1):
            sys.stdout.write(str((2 * i) - 1) + " ")
        sys.stdout.write("\n")


if __name__ == "__main__":
    test_input = """2
3
6

    """
    sys.stdin = StringIO(test_input)
    main()