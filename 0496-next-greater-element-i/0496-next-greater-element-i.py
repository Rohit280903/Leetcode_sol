class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.append(-1)
        for i in range (len(nums1)):
            flag = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = True
                if ((nums1[i] < nums2[j]) or (nums2[j] == -1)) and (flag):
                    res.append(nums2[j])
                    break
        return res
                    