"""
strstr (a.k.a find sub string), is a useful function in string operation. 
Your task is to implement this function.
For a given source string and a target string, you should output the first 
index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Example
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.
"""

def strstr(source, target):
    window = len(target)
    full = len(source)
    i = 0
    # while True:
    #     i += 1
    for i in xrange(full-window+1):
        j = 0
        while j < window:
            if source[i+j] != target[j]:
                break
            j += 1
            if j == window:
                return 1
    return -1

s1 = "source"
t1 = "target"
s2 = "abcdabcdefg"
t2 = "bcd"
print strstr(s1, t1)
print strstr(s2, t2)