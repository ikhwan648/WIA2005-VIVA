# Radix sort in Python



def radixsort(array, place):
    sizenum = len(array)
    output = [0] * sizenum
    count = [0] * 10                #O(d) = value of d ,k is the maximum possible value, then d would be O(logb(k))

#repeated for each iteration so for each iteration ( O(n) + O(k) +  0(n) +  0(n) )
    for i in range(0, sizenum):
        index = array[i] // place      #putting element into the places. We know that for this the
        count[index % 10] += 1              #end of this loop is n+1,therefore it TC is O(n)


    for i in range(1, 10):             #calculate the i + i-1
        count[i] += count[i - 1]            #O(k)


    i = sizenum - 1
    while i >= 0:                                   #0(n)

        if i == 0:
            print("")
            print("   new digit places sorting")


        index = array[i] // place
        output[count[index % 10] - 1] = array[i]            #sorting
        count[index % 10] -= 1
        i -= 1
        print(output)   #printing sorting for each number in an iteration


    for i in range(0, sizenum):
        array[i] = output[i]                #0(n)
#end of loop
#therefore the time complexity is O(d)x( O(n) + O(k) +  0(n) +  0(n) )   = O(d(n+k)))


def maximumplaces(array):
    max_num = max(array)


    place = 1
    while max_num // place > 0:
        radixsort(array, place)
        place *= 10


data = [50, 132, 174, 260, 301, 395, 409]

print(data)
print("")
print("     First sorting ")
maximumplaces(data)

print("Final result")
print(data)