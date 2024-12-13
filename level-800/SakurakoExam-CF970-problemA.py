from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        ones, twos = map(int, data[index].split()) 
        index += 1

        if (ones % 2 == 1):           
            sys.stdout.write("NO" + "\n")
            continue
        elif (ones == 0 and twos % 2 == 1):
            sys.stdout.write("NO" + "\n")
            continue
        sys.stdout.write("YES" + "\n")

if __name__ == "__main__":
    test_input = """5
0 1
0 3
2 0
2 3
3 1

    """
    sys.stdin = StringIO(test_input)
    main()