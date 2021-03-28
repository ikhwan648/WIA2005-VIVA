def kmp_matcher(string,pattern):
    n=len(string)
    m=len(pattern)
    lps=compute_prefix(pattern)
    j=0
    for i in range(n):
        while j>0 and string[i]!=pattern[j]:
            j=lps[j-1]
        if string[i]==pattern[j]:
            j+=1
        if j==m:
            print("Pattern found in index ", (i-(j-1)))
            j=lps[j-1]


def compute_prefix(pattern):
    m=len(pattern)
    lps=[0]*m
    k=0
    for i in range(1,m):
        while k>0 and pattern[k]!=pattern[i]:
            k=lps[k-1]
        if pattern[k]==pattern[i]:
            k+=1
        lps[i]=k
    return lps

string="algorithmisfun"
pattern="fun"
kmp_matcher(string,pattern)

