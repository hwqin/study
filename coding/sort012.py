
def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

##
## low, mid, high to sort 0,1,2
## use low start of 0, high as next postion of 2, mid scan
##
'''
left=0 mid=0 right= len-1
while mid <= high:
    if vmid == 0, exchange  with left left +1; mid+=1
    if vmid == 2, exchange with  right, right -=1
    else mid+1
'''
