from io import StringIO
import numpy
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
        numbers = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        sum = 0
        odd = []
        even = []

        for i in range(n):
            if numbers[i] % 2 == 1:
                odd.append(numbers[i])
            else:
                even.append(numbers[i])

        even.sort(reverse=True)
        odd.sort(reverse=True)

        if len(odd) == 0 and len(even) >= 1:
            result = 1
        else:
            for j in range(n):
                sum += 

        for i in range(n):
            sum += numbers[i]


        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """5
1
1
2
1 2
3
2 4 6
4
1000000000 999999999 999999998 999999997
10
3 1 4 1 5 9 2 6 5 3

    """
    sys.stdin = StringIO(test_input)
    main()