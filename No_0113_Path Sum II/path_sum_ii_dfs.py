'''

Description:

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of whole binary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n ).



def test_bench():

    root = TreeNode( 5 )

    root.left = TreeNode( 4 )
    root.right = TreeNode( 8 )

    root.left.left = TreeNode( 11 )

    root.right.left = TreeNode( 13 )
    root.right.right = TreeNode( 4 )

    root.left.left.left = TreeNode( 7 )
    root.left.left.right = TreeNode( 2 )

    root.right.right.left = TreeNode( 5 )
    root.right.right.right = TreeNode( 1 )

    path_of_sum = Solution().pathSum( root, s = 22 )

    # expected output:
    '''
    [[5, 4, 11, 2], [5, 8, 4, 5]]
    '''


    print( path_of_sum )

    return 



if __name__ == '__main__':

    test_bench()