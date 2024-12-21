# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = str(data[index])
        index += 1
        result = ''
        n = n[::-1]

        for i in range(len(n)):
            if n[i] == 'q':
                result += 'p'
            elif n[i] == 'p':
                result += 'q'
            else:
                result += n[i]

        sys.stdout.write(result + "\n")


if __name__ == "__main__":
#     test_input = """5
# qwq
# ppppp
# pppwwwqqq
# wqpqwpqwwqp
# pqpqpqpq

#     """
#     sys.stdin = StringIO(test_input)
    main()