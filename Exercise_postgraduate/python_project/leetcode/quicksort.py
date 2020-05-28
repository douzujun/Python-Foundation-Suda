# -*- coding: utf-8 -*-

def Partition(a, low, high):
    pivot = a[low]
    
    while (low < high):
        while (low < high and a[high] >= pivot):
            high = high - 1
        a[low] = a[high]
        while (low < high and a[low] <= pivot):
            low = low + 1
        a[high] = a[low]
    
    a[low] = pivot
    
    return low

def Qsort(a, low, high):
    pivotloc = Partition(a, low, high)
    
    if (low < high):
        pivotloc = Partition(a, low, high)
        Qsort(a, low, pivotloc - 1)
        Qsort(a, pivotloc + 1, high)
        
def QuickSort(a, size):
    Qsort(a, 0, size - 1)
    for e in a:
        print(e, end=" ")
    
def main():
    a = list(range(0, 10))
    a.reverse()
    print(a)
    QuickSort(a, len(a))
    
    
main()
        
