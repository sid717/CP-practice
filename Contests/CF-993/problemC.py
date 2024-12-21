# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        m, a, b, c = map(int, data[index].split()) 
        index += 1
        
        seated_a = min(a,m)
        seated_b = min(b,m)
        seated_c = min((m*2) - (seated_a + seated_b), c)

        seated_max = seated_a + seated_b + seated_c

        sys.stdout.write(str(seated_max) + "\n")


if __name__ == "__main__":
#     test_input = """5
# 10 5 5 10
# 3 6 1 1
# 15 14 12 4
# 1 1 1 1
# 420 6 9 69

#     """
#     sys.stdin = StringIO(test_input)
    main()