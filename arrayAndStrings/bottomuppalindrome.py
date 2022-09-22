
def longest_palindrome(s):
    n = len(s)
    table = [[ 0 for i in range(n)] for j in range(n)]
    start = 0
    maxLength = 2

    # for length=1
    for i in range(n):
        table[i][i] = True

    # for length =2
    for i in range(n-1):
        if s[i]== s[i+1]:
            table[i][i+1] = True
            start = i
            maxLength = 2

    # for length >3
    k = 3
    while(k <= n):
        i = 0
        while(i < n-k+1):
            j = i+k-1
            # print(i, j)
            # print(table[i+1][j-1])
            if (table[i+1][j-1] and 
                s[i] == s[j]):
                table[i][j] = True
                if k > maxLength:
                    start= i
                    maxLength = k
            i+=1
        k+=1
    return s[i-1:i+maxLength-1]

s = "abcdcba"
print(longest_palindrome(s))
