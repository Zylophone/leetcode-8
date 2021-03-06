'''

Description:

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''


from typing import List
class Solution:
    
    
    def reverse(self, nums: List[int], start, end):
        
        while start < end:
            
            nums[start], nums[end] = nums[end], nums[start]
            
            start += 1
            end -= 1
            
            
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        
        if k > size:
            # eliminate redundant rotation which is over size
            k = k % size 
        
        
            # reverse all elements
        self.reverse( nums, 0, size-1)
        
            # reverse first k elements
        self.reverse( nums, 0, k-1)
        
            # reverse last (size - k) elements 
        self.reverse( nums, k, size-1)
        
        return



# N : the length of input array nums
# k : the times of rotation

## Time complexity: O( N )
#
# The overhead is the for loop on k of O( k ), but it is reduce to O( N ) no matter how large is k.

## Space complexity: O( 1 )
#
# The overhead is the variable for reverse operation



def test_bench():

    test_data = [ 
                    ([1, 3, 5, 7, 9], 2),
                    ([1, 3, 5, 7, 9], 11)
                ]

    # expected output:
    '''
    [7, 9, 1, 3, 5]
    [9, 1, 3, 5, 7]
    '''

    for test in test_data:

        Solution().rotate( test[0], test[1] )
        print( test[0] )

    
    return



if __name__ == '__main__':

    test_bench()