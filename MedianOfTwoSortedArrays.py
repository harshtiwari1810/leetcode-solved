class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        mergeList = nums1 + nums2
        mergeList.sort()
        
        if (len(mergeList)%2 != 0):
            mid = len(mergeList)//2
            return mergeList[mid]
        else:
            mid = int(len(mergeList)/2)
            ans = (mergeList[mid] + mergeList[mid-1])/2
            return ans

