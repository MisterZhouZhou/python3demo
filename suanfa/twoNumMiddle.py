# 取两个数组中的中值
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        t = nums1 + nums2
        t.sort()
        l = len(t)
        medinum = l // 2 # // 为取整运算符
        if l%2 == 1:
            return t[medinum]
        else:
            return (t[medinum-1]+t[medinum])/2.0

if __name__ == "__main__":
    solution = Solution()
    array1 = [1,2]
    array2 = [3,4]
    result = solution.findMedianSortedArrays(array1, array2)
    print(result)