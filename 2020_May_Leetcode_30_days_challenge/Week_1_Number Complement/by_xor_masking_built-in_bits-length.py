'''

Description:

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

'''



from math import log
from math import floor

class Solution:
    def findComplement(self, num: int) -> int:

        bits_length = num.bit_length()

        return num^( 2 ** bits_length - 1 )




# n : the value of input number

## Time Complexity: O( log n )
#
# The overhead in time is the cost of bit scan, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bit-mask, which is of O( 1 )



def test_bench():

    test_data = [ 1,2,3,4,5,6,7,8,9,10,11,128]

    # expected output:
    '''
    0
    1
    0
    3
    2
    1
    0
    7
    6
    5
    4
    127
    '''


    for number in test_data:

        print( Solution().findComplement( number ) )
    
    return 




if __name__ == '__main__':

    test_bench()        