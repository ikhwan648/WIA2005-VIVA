def kmp_matcher(string,pattern):
    n=len(string)
    m=len(pattern)
    prefixArray=compute_prefix(pattern)
    j=0
    for i in range(n):
        while j>0 and string[i]!=pattern[j]:
            j=prefixArray[j-1]
        if string[i]==pattern[j]:
            j+=1
        if j==m:
            print("Pattern found in index ", (i-(j-1)))
            j=prefixArray[j-1]


def compute_prefix(pattern):
    m=len(pattern)
    lps=[0]*m
    k=0
    for i in range(1,m):
        if pattern[k]==pattern[i]:
            k+=1
            lps[i]=k
        else:
            k=0
            lps[i]=k
    return lps


string="algorithmisfun"
pattern="fun"
kmp_matcher(string,pattern)

