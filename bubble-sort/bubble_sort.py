def bubble (nums):
    size = len(nums)
    for _ in nums:
        sorted = True
        print(nums)
        for i in range(size-1):
            if nums[i] > nums[i+1]:
                sorted = False
                nums[i+1], nums[i] = nums [i] , nums[i+1]
        if sorted:
            return nums

bubble([1,2,3,4,5])
