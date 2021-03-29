def kmp_matcher(string,pattern):
    n=len(string)
    m=len(pattern)
    lps=compute_prefix(pattern)
    print(lps)
    j=0                                                     # number of characters matched
    for i in range(n):                                      # scan the text from left to right
        while j>0 and string[i]!=pattern[j]:                
            j=lps[j-1]                                      # next character does not match
        if string[i]==pattern[j]:
            j+=1                                            # next character matches
        if j==m:                                            # is all of pattern matched?
            print("Pattern found in index ", (i-(j-1)))    
            j=lps[j-1]                                      # look for the next match


def compute_prefix(pattern):
    m=len(pattern)
    lps=[0]*m
    k=0                                                     # number of character and suffix
    for i in range(1,m):
        while k>0 and pattern[k]!=pattern[i]:
            k=lps[k-1]                                      # find previous suffix
        if pattern[k]==pattern[i]:
            k+=1                                            # next character and lps value
        lps[i]=k                                            # store k in lps[]
    return lps

string="algorithmisfun"
pattern="fun"
kmp_matcher(string,pattern)

