import time

def RabinKarp(string, searchPattern, Q):

    m = len(searchPattern)
    n = len(string)
    R = 10
    RM = 1
    p = 0 #hash value for searchPattern
    t = 0 #hash value for string

    for i in range((m-1)): #obtain the result of *10 power of m-1
        RM = (RM*R)%Q
    print("RM: " + str(RM))

    for i in range(0, m):
        print("[p] i: "+str(i)+" char: "+searchPattern[i]+" ascii: "+str(ord(searchPattern[i])))
        print("[t] i: " +str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        p=(R*p + ord(searchPattern[i]))%Q
        t=(R*t + ord(string[i]))%Q
        print("p: "+str(p))
        print("t: "+str(t)+"\n")

    if p==t:
        return "found at index 0"

    print("Hash for pattern: "+str(p))

    for i in range(m, n): #after the m index, calculate for t only
        t=( (t- RM * ( ord(string[i-m]) ) ) * R + ord(string[i]) ) % Q
        print("[t] i: " +str(i)+" char: "+string[i]+" ascii: "+str(ord(string[i])))
        print("t: "+str(t))
        if p==t:
            return "found at index "+ str(i-m+1)

string = "algorithmisfun"
searchPattern = "fun"
Q = 997
start = time.time()
index = RabinKarp(string, searchPattern, Q)
end = time.time()
print("\n"+str(index)+ " with the running time of "+str(end-start))