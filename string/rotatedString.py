# rotatedString
'''
Given "abcdefg".
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
'''


class Solution:
    """
    param A: A string
    param offset: Rotate string with offset.
    return: Rotated string.
    """
    def rotateString(self, A, offset):
        if len(A) == 0:
            return A
        # do not modulo zero, so check first
        offset = offset % len(A)
        # if offset = 0, result form is wrong
        if offset == 0:
            return A
        result = A[-offset:] + A[:len(A) - offset]
        return result

Sol = Solution()
print Sol.rotateString("", 6)