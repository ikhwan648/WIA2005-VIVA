#Counting Sort
def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array sampai no berapa
    count = [0] * 1000

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 1000):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

num = [47, 25, 34, 92, 31, 31,0, 1,3,9,100,8,47,1,3,60,7,99,22,99]
countingSort(num)
print("Sorted Array in Ascending Order: ")
print(num)