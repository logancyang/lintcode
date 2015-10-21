class Cell:

    def __init__(self, x, y, prev=None, value=None):
        # prev = [Cell]
        self.prev = prev
        self.cellIndex = (x, y)
        self.value = value

    def __str__(self):
        return str(self.value) +", " + str(self.cellIndex) + ", " + str(self.prev)

    def get_value():
        return self.value

    def set_value(prev, value):
        if prev != []:
            self.value = sum(prev.get_value())
        else:
            self.value = value

Cell1 = Cell(1, 1, value=1)
# print Cell1

"""
a * 33^3 + b * 33^2 + c * 33 + d
-->
0 * 33 + a
a * 33 + b
a * 33^2 + b * 33 + c
a * 33^3 + b * 33^2 + c * 33 + d
"""

def hashCode(key, HASH_SIZE):
    hashvalue = 0
    for i in xrange(len(key)):
        hashvalue = hashvalue * 33 + ord(key[i])
        hashvalue %= HASH_SIZE
    return hashvalue

"""
A1 + B2 + C$4
"""
key = "abcd"
print hashCode(key, 1000)
key = "abd"
print hashCode(key, 1000)
key = "acdee"
print hashCode(key, 1000)