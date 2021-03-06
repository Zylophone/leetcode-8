'''

Description:

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''



from itertools import combinations

class Solution:
    def subsets(self, nums):
        
        solution, size = [], len(nums)
        
        for k in range(size+1):
            
            solution += [ list(comb) for comb in combinations(nums, k) ]
        
        return solution



# n : the length of input array, nums.

## Time Complexity: O( n * (2^n) )
#
# The overhead in time is the cost of subset generation, which is of O( n * (2^n) ).

## Space Complexity: O( 2^n )
#
# The overhead in space is the storage for output list, solution, which is of O( 2^n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'elements')
def test_bench():

    test_data = [
                    TestEntry( elements = [] ),
                    TestEntry( elements = [ 1] ),
                    TestEntry( elements = [ 1, 2] ),
                    TestEntry( elements = [ 1, 2, 3] ),
                ]

    for t in test_data:

        print( Solution().subsets( nums = t.elements ) )

    return 



if __name__ == '__main__':

    test_bench()