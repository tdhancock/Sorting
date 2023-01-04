def quicksort(lyst):
    lyst1 = list(lyst)
    length = len(lyst)
    if length <= 1:
        return lyst
    else:
        pivot = lyst1.pop()
    bigger = []
    smaller = []
    for x in lyst1:
        if x > pivot:
            bigger.append(x)
        else:
            smaller.append(x)
    return quicksort(smaller) + [pivot] + quicksort(bigger)

def mergesort(lyst):
    def merge(left, right):
        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result

    if len(lyst) <= 1:
        return lyst
    half = len(lyst) // 2
    left = mergesort(lyst[:half])
    right = mergesort(lyst[half:])

    return merge(left, right)

def selection_sort(lyst):
    length = range(0, len(lyst) - 1)
    for x in length:
        minVal = x
        for i in range(x+1, len(lyst)):
            if lyst[i] < lyst[minVal]:
                minVal = i
        if minVal != x:
            lyst[minVal] , lyst[x] = lyst[x], lyst[minVal]
        
    return lyst

def insertion_sort(lyst):
    length = range(1, len(lyst))
    for x in length:
        value = lyst[x]

        while lyst[x-1] > value and x > 0:
            lyst[x], lyst[x-1] = lyst[x-1] , lyst[x]
            x = x-1

    return lyst

def is_sorted(lyst):
    val = (all(isinstance(item, int) for item in lyst))
    if not val:
        return False
    if (sorted(lyst) == lyst):
        return True
        
    return False

