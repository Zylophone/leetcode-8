'''

Description:

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.

'''



class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        words = []
        
        vowel = set('AEIOUaeiou')
        
        for idx, word in enumerate(S.split(), 1):
            
            if word[0] in vowel:
                # postfix for vowel heading
                word = word + 'ma'
            
            else:
                # postfix for non-vowel heading
                word = word[1:] + word[0] + 'ma'
            
            
            # general common postfix
            word = word + 'a' * idx
            
            words.append(word)
            
        return ' '.join(words)



# n: the character length of input, S

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n^2 )
#
# The overhead in space is the storage for output list, which is of O( n^2 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().toGoatLatin( S="I speak Goat Latin" )
        self.assertEqual(result, "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")

    
    def test_case_2(self):

        result = Solution().toGoatLatin( S="The quick brown fox jumped over the lazy dog" )
        self.assertEqual(result, "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")



if __name__ == '__main__':

    unittest.main()