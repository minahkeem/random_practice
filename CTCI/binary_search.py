#binary search implementation

def search(lst, val):
    return binary_search(lst, val, 0, len(lst)-1)

def binary_search(lst, val, low, high):
    if(low == high):
        return False
    mid = int((low+high)/2)
    if(lst[mid]==val):
        return True
    elif(lst[mid]<val):
        return binary_search(lst, val, mid+1, high)
    else:
        return binary_search(lst, val, low, mid)

def main():
    lst = [1, 3, 6, 17, 100, 236, 540]
    print(search(lst, 3))
    print(search(lst, 2))
    print(search(lst, -1))
    print(search(lst, 600))
    print(search(lst, 100))
    
main()