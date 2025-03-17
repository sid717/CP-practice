from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index]) #for individual value
        index += 1
        s = data[index] #for inputting into a string
        index += 1

        eyecount = 0
        mouthcount = 0

        for i in range(n):
            if s[i] == '_':
                mouthcount += 1
            else:
                eyecount += 1   

        if n < 3 or eyecount < 2 or mouthcount < 1:
            result = 0
        else:
            result = ((eyecount - 1) * mouthcount) + (eyecount - 2)

        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """8
3
--_
5
__-__
9
--__-_---
4
_--_
10
_-_-_-_-_-
7
_------
1
-
2
_-

    """
    sys.stdin = StringIO(test_input)
    main()