from multiprocessing import reduction


def longestPalindrome(s: str):
    lar_res = ""
    for i in range(len(s)):
        #for odd
        res = checkPalindrome(s, i, i)
        if len(res)> len(lar_res):
            lar_res = res

        res = checkPalindrome(s, i, i+1)
        if len(res)> len(lar_res):
            lar_res = res
    return lar_res

def checkPalindrome(s, l, r):
    while(l>=0 and r < len(s) and s[l] == s[r]):
        l-=1
        r+=1
    return s[l+1:r]

s = "abba"
print(longestPalindrome(s))

