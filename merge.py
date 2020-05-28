# Merge sort a list
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        merge_sort(left)
        merge_sort(right)
        left_pointer=right_pointer=sorted_pointer=0
        while(left_pointer<len(left) and right_pointer<len(right)):
            if left[left_pointer]<right[right_pointer]:
                nums[sorted_pointer]=left[left_pointer]
                left_pointer += 1
            else:
                nums[sorted_pointer]=right[right_pointer]
                right_pointer += 1
            sorted_pointer += 1
        if len(left):
            while(left_pointer<len(left)):
                nums[sorted_pointer]=left[left_pointer]
                left_pointer += 1
                sorted_pointer += 1
        if len(right):
            while(right_pointer<len(right)):
                nums[sorted_pointer]=right[right_pointer]
                right_pointer += 1
                sorted_pointer += 1
        return nums
    else:
        return nums
print(merge_sort([23,11,10,5,9,7]))