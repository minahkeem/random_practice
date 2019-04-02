def find_pair(int_list, num):
    l = 0
    r = len(int_list)-1
    max_sum = (int_list[r]+int_list[l], l, r)
    while r > l:
        print(max_sum[0])
        if max_sum[0] > num:
            r -= 1
        elif max_sum[0] < num:
            l += 1
        else:
            break
        if r > l:
            curr_val = int_list[r] + int_list[l]
            if curr_val < num and max_sum[0] < curr_val or max_sum[0] > num:
                max_sum = (curr_val, l, r)
    return int_list[max_sum[1]], int_list[max_sum[2]]

def main():
    lst1 = [4, 10, 23, 25, 60, 80, 95]
    lst2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst3 = [0, 10, 19, 34, 49]
    
    print(find_pair(lst1, 60))
    print(find_pair(lst2, 60))
    print(find_pair(lst3, 60))
    
main()