def fastsort(arr):
    if len(arr)<1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return fastsort(left)+middle+fastsort(right)

list1=fastsort([2,6,3,1,9,3])
if __name__=='__main__':
    print(list1)
