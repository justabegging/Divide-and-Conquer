import random, time

def mergeSort(arr):
    print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j +1
            k = k + 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        print("Merging ", arr)

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    #print("Done merging: ", result[:3])
    return result

def mergesort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr)/2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    #print("Going to merge: ", merge(left, right))
    return merge(left, right)

def testStation(arr):
    timeStamps = []
    timeStamp = time.clock()
    mergesort(arr)
    timeStamp = time.clock() - timeStamp
    timeStamps.append(timeStamp)
    print("Done! It took: ", timeStamps)
    
def main():
    arr = []
    left = []
    right = []
    for i in range(0,100000):
        arr.append(i)
    random.shuffle(arr)
    testStation(arr)
    
    
    #print(arr)
    #mergesort(arr)
    #print("Done")

main()
