# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    sizenum = len(array)
    output = [0] * sizenum
    count = [0] * 10


    for i in range(0, sizenum):
        index = array[i] // place      #putting element into the places
        count[index % 10] += 1


    for i in range(1, 10):             #calculate the i + i-1
        count[i] += count[i - 1]


    i = sizenum - 1
    while i >= 0:

        if i == 0:
            print("         new iteration")
            print("")

        index = array[i] // place
        output[count[index % 10] - 1] = array[i]            #sorting
        count[index % 10] -= 1
        i -= 1
        print(output)   #sini


    for i in range(0, sizenum):
        array[i] = output[i]



def radixSort(array):
    max_element = max(array)


    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [50, 131, 151, 231, 301, 395, 401]

print(data)
print("")

radixSort(data)
print(data)