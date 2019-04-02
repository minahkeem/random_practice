#MERGE SORT

def mergesort(lst):
    helper = []
    mergesort_helper(lst, helper, 0, len(lst)-1)
    
def mergesort_helper(lst, helper, low, high):
    if(low == high):
        return
    mid = (low+high)//2
    mergesort_helper(lst, helper, low, mid)
    mergesort_helper(lst, helper, mid+1, high)
    merge(lst, helper, low, mid, high)
    
def merge(lst, helper, low, mid, high):
    for i in range(low, high+1):
        helper.append(lst[i])
    l = low
    r = mid+1
    for i in range(low, high+1):
        if(l > mid or r > high):
            break
        if(helper[l-low] < helper[r-low]):
            lst[i] = helper[l-low]
            l += 1
        else:
            lst[i] = helper[r-low]
            r += 1
    print(helper)
    helper = []
        
def main():
    lst1 = [3, 1, 5, 7, 2, 4, 9, 6]
    print('Before: ', lst1)
    mergesort(lst1)
    print('After: ', lst1)
    print('--------------------------------')
    lst2 = [2, 1, 2, 4, 9, 3, 7, 2, 8]
    print('Before: ', lst2)
    mergesort(lst2)
    print('After: ', lst2)
    
main()