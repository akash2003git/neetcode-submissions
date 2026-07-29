class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
          freq = hash_map.get(num)
          if freq == 1:
            return True
          else:
            hash_map[num] = 1
        return False