# 10.1 Sorted Merge
def sorted_merge(A, B, lenA, lenB):
    i = lenA - 1
    j = lenB - 1
    k = lenA + lenB - 1
    while(j >= 0 and i >= 0):
        if(B[j] > A[i]):
            A[k] = B[j]
            k -= 1
            j -= 1
        else:
            A[k] = A[i]
            k -= 1
            i -= 1

def main():
    A = [1, 3, 5, 8] + [None]*6
    B = [2, 4, 6, 7, 10]
    
    sorted_merge(A, B, 4, 5)
    print(A)
    
main()