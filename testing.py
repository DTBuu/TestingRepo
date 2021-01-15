def isPld(x):
    left = 0
    right = len(x) - 1
    while (left<right):
        if (x[left]!=x[right]):
            return 0
        left += 1
        right -= 1
    return 1
def lenLongestPld(x):
    n = len(x)
    for mould_size in range(n, 1, -1):
        a = 0
        b = a + mould_size
        while(b <= n):
            if(isPld(x[a:b])):
                return len(x[a:b])
            a += 1
            b = a + mould_size
    return 1

input_str = input()
print(lenLongestPld(input_str))