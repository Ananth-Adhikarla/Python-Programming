"""
Merge Sort
"""

def merge_sort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1



alist = [54,26,93,17,77,31,44,55,20]

print("Original list ",alist)

merge_sort(alist)

print("Sorted List ", alist)

blist = [98, 744, 28, 81, 447, 2, 5, 10, 99, 55]

print("Original list ",blist)

merge_sort(blist)

print("Sorted List ", blist)
