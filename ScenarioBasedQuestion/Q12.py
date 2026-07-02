"""Please write a binary search function which searches an item in a sorted list.
 The function should return the index of element to be searched in the list."""


def binarySearch(u:list,taget:int):
    left = 0
    right = len(u)-1

    while left<=right:
        mid = (right + left) // 2
        if u[mid]==taget:
            return mid
        elif taget>=u[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1

result = binarySearch([1,2,3,4,5,6],2)
if result!=-1:
    print(f"index is {result}")

