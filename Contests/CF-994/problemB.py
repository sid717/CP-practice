from io import StringIO
import sys

def check_ps(string):
    p_index = string.find('p')
    if p_index != -1:
        for i in range(p_index + 1, len(string)):
            if string[i] == 's':
                return "NO"
    return "YES"

def is_permutation(array, i):
    


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
        
        s_count = s.count("s")
        p_count = s.count("p")
        period_count = s.count(".")

        if s_count == n or p_count == n or period_count == n:
            result = "YES"
        elif s_count == 0 or p_count == 0:
            result = "YES"

        # elif s[0] == 'p' and s[n-1] == 's':
        #     result = "NO"
        # elif p_count >= 1 and s[n-1] == 'p':
        #         result = "YES"
        # else:
        #      result = "NO"

        # sys.stdout.write(result + "\n")


if __name__ == "__main__":
    test_input = """9
4
s.sp
6
pss..s
5
ppppp
2
sp
4
.sp.
8
psss....
1
.
8
pspspsps
20
....................

    """
    sys.stdin = StringIO(test_input)
    main()