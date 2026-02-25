class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def custom_sort(n):
            bit_cnt = bin(n).count('1')
            return (bit_cnt, n)
        
        arr.sort(key=custom_sort)

        return arr