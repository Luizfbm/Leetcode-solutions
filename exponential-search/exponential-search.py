def search(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    r = 1
    while r < n and arr[r] < target:
        r *= 2     
    if arr[r] == target:
        return r
    return search(arr, target ,r//2, min(r,n-1))


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
target = 32
result = exponential_search(arr, target)

print(f"Element found at index {result}")
