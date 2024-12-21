from io import StringIO
import sys
from collections import Counter

def find_mode(arr, i):
    freq_dict = Counter(arr[:i+1])
    mode = freq_dict.most_common(1)[0][0]
    return mode

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index]) 
        index += 1
        array_a = list(map(int, data[index].split())) 
        index += 1
        array_b1 = [array_a[0]]

        from collections import Counter
        
        array_b = []
        counter = Counter()
        
        while True:
            # append elements to array_b
            element = # get the next element to append
            array_b.append(element)
        
            # update the counter
            counter[element] += 1
        
            # print the current counter
            print(counter)

        for i in range(n):
            array_b.append()
            sys.stdout.write(str(find_mode(array_a, i)) + " ")

        sys.stdout.write("\n")


if __name__ == "__main__":
    test_input = """4
2
1 2
4
1 1 1 2
8
4 5 5 5 1 1 2 1
10
1 1 2 2 1 1 3 3 1 1

    """
    sys.stdin = StringIO(test_input)
    main()