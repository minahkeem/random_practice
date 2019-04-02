#8.2 Robot in a Grid
def find_path(arr):
    path = [(0,0)]
    helper(arr, path, 0, 0)
    reverse_list(path)
    return path

def helper(arr, path, x, y):
    if arr[x][y] == 1:
        if x == len(arr)-1 and y == len(arr[0])-1:
            path.append((x,y))
            return 1
        r, d = 0, 0
        if x == len(arr)-1:
            r, d = arr[x][y+1], 0
        elif y == len(arr[0])-1:
            r, d = 0, arr[x+1][y]
        else:
            r, d = arr[x][y+1], arr[x+1][y]
        if r == 0 and d == 0:
            path.pop()
            return -1
        elif r == 0 and d == 1:
            check_val = helper(arr, path, x+1, y)
            if check_val == -1:
                path.pop()
                return -1
            else:
                path.append((x, y))
                return 1
        elif r == 1 and d == 0:
            check_val = helper(arr, path, x, y+1)
            if check_val == -1:
                path.pop()
                return -1
            else:
                path.append((x, y))
                return 1
        else:
            check_val = helper(arr, path, x+1, y)
            if check_val == -1:
                check_val = helper(arr, path, x, y+1)
                if check_val == -1:
                    path.pop()
                    return -1
                else:
                    path.append((x, y))
                    return 1
            else:
                path.append((x, y))
                return 1

def reverse_list(arr):
    i, j = 0, len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def main():
    grid1 = [[1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [0, 1, 1, 1, 1]]
    
    grid2 = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 1]]
    
    path1 = find_path(grid1)
    path2 = find_path(grid2)
    
    print("Grid 1 path: ", path1)
    print("Grid 2 path: ", path2)
    
main()