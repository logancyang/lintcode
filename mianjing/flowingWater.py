__author__ = 'loganyang'

# Flowing Water:
# Find the coordinates of the points which can flow both to the Pac and the Atl oceans
# Pacific: ~
# Atlantic: *
# Input:
#
# ~  ~   ~   ~   ~   ~  ~
# ~  1   2   2   3  (5) *
# ~  3   2   3  (4) (4) *
# ~  2   4  (5)  3   1  *
# ~ (6) (7)  1   4   5  *
# ~ (5)  1   1   2   4  *
# *  *   *   *   *   *  *
# Note: lower-left and upper-right can reach both oceans
# Pacific: [0, j], [i, 0]
# Atlantic: [n-1, j], [i, n-1]

# Output:
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

# brute force: dfs twice for Pac and Atl for each point
class Brute:

    def flowingWater(self, inputMat):
        result = []
        if inputMat is None or len(inputMat) == 0:
            return result
        for i in xrange(len(inputMat)):
            for j in xrange(len(inputMat[0])):
                if self.check(inputMat, i, j):
                    result.append([i, j])
        return result

    def check(self, inputMat, i, j):
        nrow = len(inputMat)
        ncol = len(inputMat[0])
        # the two corners
        if i == 0 and j == ncol - 1:
            return True
        if i == nrow - 1 and j == 0:
            return True
        # set of tuples (i, j)
        visited = set()
        return self.dfs(inputMat, i, j, visited, "pac") and self.dfs(inputMat, i, j, visited, "atl")

    # dfs, start at (i, j), end at a border. Can only go down hill
    def dfs(self, inputMat, i, j, visited, ocean):
        nrow = len(inputMat)
        ncol = len(inputMat[0])
        visited.add((i, j))
        if i < 0 or i >= nrow or j < 0 or j >= ncol:
            return False
        # base cases: Success
        if (i == 0 or j == 0) and ocean == "pac":
            return True
        if (i == nrow - 1 or j == ncol - 1) and ocean == "atl":
            return True
        # recursion
        # bug1: if i, j is on the border but not the correct ocean, return False directly is wrong
        # should still recurse to other places to see if correct ocean can be reached
        if i - 1 >= 0 and inputMat[i-1][j] <= inputMat[i][j] and (i-1, j) not in visited:
            # bug3: DO NOT "return dfs" when dfs is boolean!!
            # Because if it's False, upper level returns False and do not recurse to other routes!!
            # put boolean dfs in condition instead!
            if self.dfs(inputMat, i-1, j, visited, ocean):
                return True
        # NOT elif!! or the recursion only has 1 way down!!
        # bug2: for i-1 and i+1, the conditions are both <=, then if ==, infinite loop!!
        # record visited positions!
        if i + 1 < nrow and inputMat[i+1][j] <= inputMat[i][j] and (i+1, j) not in visited:
            if self.dfs(inputMat, i+1, j, visited, ocean):
                return True
        if j - 1 >= 0 and inputMat[i][j-1] <= inputMat[i][j] and (i, j-1) not in visited:
            if self.dfs(inputMat, i, j-1, visited, ocean):
                return True
        if j + 1 < ncol and inputMat[i][j+1] <= inputMat[i][j] and (i, j+1) not in visited:
            if self.dfs(inputMat, i, j+1, visited, ocean):
                return True
        return False

# better
# search from outside, reverse the flow
# the intersection of the sets of points reachable by both pac and atl is the result
class Solution:

    def flowingWater(self, mat):
        result = []
        if mat is None or len(mat) == 0:
            return result
        nrow = len(mat)
        ncol = len(mat[0])
        pac_set = set()
        atl_set = set()
        # pac points: (0, j), (i, 0)
        for j in xrange(ncol):
            pac_set.add((0, j))
            self.dfs(mat, 0, j, pac_set)

        for i in xrange(nrow):
            pac_set.add((i, 0))
            self.dfs(mat, i, 0, pac_set)

        # atl points: (n-1, j), (i, n-1)
        for j in xrange(ncol):
            atl_set.add((nrow - 1, j))
            self.dfs(mat, nrow - 1, j, atl_set)

        for i in xrange(nrow):
            atl_set.add((i, ncol - 1))
            self.dfs(mat, i, ncol - 1, atl_set)

        result_set = pac_set.intersection(atl_set)
        result = list(result_set)
        # return pac_set, atl_set
        return result

    # reverse flow dfs, go to larger '>' points
    # modify set 'visited'
    def dfs(self, mat, i, j, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        nrow = len(mat)
        ncol = len(mat[0])
        # base case
        if i < 0 or i >= nrow or j < 0 or j >= ncol:
            pass
        # recursion
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i < 0 or new_i >= nrow or new_j < 0 or new_j >= ncol:
                continue
            if mat[new_i][new_j] < mat[i][j] or (new_i, new_j) in visited:
                continue
            visited.add((new_i, new_j))
            self.dfs(mat, new_i, new_j, visited)
            # bug: do not undo the change in this case
            # because dfs need to modify it after execution
            # visited.discard((new_i, new_j))


inputMat1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

# Sol = Brute()
# print inputMat1[0][1]
# print Sol.dfs(inputMat1, 1, 4, set(), "pac")
# print Sol.dfs(inputMat1, 0, 1, set(), "atl")
# print Sol.check(inputMat1, 1, 4)
# print Sol.flowingWater(inputMat1)
Sol = Solution()
print Sol.flowingWater(inputMat1)




