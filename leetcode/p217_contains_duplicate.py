
class Solution:
    def containsDuplicate(self, nums):
        vistos = set()

        for num in nums:
            if num in vistos:
                return True
            vistos.add(num)

        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))  # True
print(s.containsDuplicate([1, 2, 3, 4]))  # False