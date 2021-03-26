def kmp_matcher(string,pattern):
    n=len(string)
    m=len(pattern)
    prefixArray=[0]*m
    prefix(pattern)
    x,y,q=0,0,0
    while x<n:
        if string[x]==pattern[y]:
            x+=1
            y+=1
        if y==m:
            print("Found pattern at index "+ str(x-y))
            y=prefixArray[y-1]
        elif x<n and string[x]!=pattern[y]:
            if y!=0:
                y=prefixArray[y-1]
            else:
                x+=1


def prefix(pattern):
    m=len(pattern)
    prefixArray=[0]*m
    prefixArray[0]=0
    k=0
    for x in range(m):
        if(pattern[x]==pattern[k]):
            k+=1
            prefixArray[x]=k
        else:
            if k!=0:
                k=prefixArray[k-1]
                x-=1
            else:
                prefixArray[x]=0


string="algorithmisfun"
pattern="fun"
kmp_matcher(string,pattern)

