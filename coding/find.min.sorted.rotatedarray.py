class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        return self.findminvalue(nums, 0, len(nums)-1)
    
    def findminvalue(self, arr, start_index, end_index):
        if start_index == end_index:
            return arr[start_index]
        
        mid_index = int((start_index+end_index)/2)
        mid_value = arr[mid_index]
        start_value = arr[start_index]
        end_value = arr[end_index]
        
        if (mid_value < start_value): # meaning min value is on first half
            return self.findminvalue(arr, start_index+1, mid_index)
        elif mid_value == start_value:
            # just compare mid and end as there are just two elements
            return min(start_value, end_value)
        else:
            if (start_value < end_value): # min value in left half
                return self.findminvalue(arr, start_index, mid_index-1)
            else: # min value in second half
                return self.findminvalue(arr, mid_index+1, end_index)
