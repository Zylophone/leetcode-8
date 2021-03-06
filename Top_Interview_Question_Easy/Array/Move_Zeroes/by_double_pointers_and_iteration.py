'''

Description:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.



   Hint #1  
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.



   Hint #2  
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

'''



from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        prev, zero_len = None, 0

        for idx, number in enumerate(nums):

            if number == 0:
                
                if prev == 0:
                    zero_len += 1
                    
                else:
                    # update previous number
                    prev = 0
                    zero_len = 1
            
            else:

                if zero_len:
                    # swap zero and non-zero elements
                    nums[ idx ], nums[ idx-zero_len ] = nums[ idx-zero_len ], nums[ idx]
                    
                else:
                    # update previous number
                    prev = number



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (i, x), which is of O( n ).

## Space Complexity: O( 1 )
# 
# The overhead in space is the zero length counter as well as swapping buffer, which is of O( 1 ).
 


def test_bench():

    test_data = [
                    [0,1,0,3,12],
                    [0,1,0,1,0],
                    [0,1,0,0,2],
                    [1,0,2,0,3],
                    [1,0,2,0,0,3],
                    [0,0,0,0,1,2],
                    [0,0,0,0,0,2]
                ]

    # expected output:
    '''
    [1, 3, 12, 0, 0]
    [1, 1, 0, 0, 0]
    [1, 2, 0, 0, 0]
    [1, 2, 3, 0, 0]
    [1, 2, 3, 0, 0, 0]
    [1, 2, 0, 0, 0, 0]
    [2, 0, 0, 0, 0, 0]
    '''
    for sequence in test_data:
        
        Solution().moveZeroes(sequence) 
        print( sequence )
    
    return



if __name__ == '__main__':

    test_bench()                    