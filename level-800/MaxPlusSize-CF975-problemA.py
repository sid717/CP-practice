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
        array = list(map(int, data[index].split()))
        index += 1
        maxIndex = array.index(max(array))
        i = 0
        colored = []
        while i <= n:
            colored.append(array[i])
            i += 2

        for i in range(n):
            if array[i] == array[i+1] or array[i] == array[i-1]:
                continue
            else:
                colored.append(array[i])

        score = max(colored) + len(colored)


        sys.stdout.write(str(score) + "\n")

if __name__ == "__main__":
    test_input = """4
3
5 4 5
3
4 5 4
10
3 3 3 3 4 1 2 3 4 5
9
17 89 92 42 29 92 14 70 45

    """
    sys.stdin = StringIO(test_input)
    main()