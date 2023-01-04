from random import seed, shuffle, sample
from time import perf_counter

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

def main():
    DATA_SIZE = 10000 
    seed(0)
    DATA = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    test = DATA.copy()   

    print("Starting quicksort")
    shuffle(test)
    start = perf_counter()
    quicksort(test)
    end = perf_counter() - start
    print(f"quicksort duration: {end} seconds")

    print("Starting mergesort")
    shuffle(test)
    start = perf_counter()
    mergesort(test)
    end = perf_counter() - start
    print(f"merge duration: {end} seconds")

    print("Starting selection_sort")
    shuffle(test)
    start = perf_counter()
    selection_sort(test)
    end = perf_counter() - start
    print(f"selection_sort duration: {end} seconds")

    print("Starting insertion_sort")
    shuffle(test)
    start = perf_counter()
    insertion_sort(test)
    end = perf_counter() - start
    print(f"insertion_sort duration: {end} seconds")

    print("Starting is_sorted")
    shuffle(test)
    start = perf_counter()
    is_sorted(test)
    end = perf_counter() - start
    print(f"is_sorted duration: {end} seconds")
    
if __name__ == "__main__":
    main()