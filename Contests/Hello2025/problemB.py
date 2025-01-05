from io import StringIO
import sys

def frequency_array(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return list(freq.values())

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

        freq_arr = frequency_array(numbers)

        while k and freq_arr:
            min_val = min(freq_arr)
            if min_val <= k:
                k -= min_val
                freq_arr.remove(min_val)

        result = len(freq_arr)
        
        sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
    test_input = """6
1 0
48843
3 1
2 3 2
5 3
1 2 3 4 5
7 0
4 7 1 3 2 4 1
11 4
3 2 1 4 4 3 4 2 1 3 3
5 5
1 2 3 4 5

    """
    sys.stdin = StringIO(test_input)
    main()