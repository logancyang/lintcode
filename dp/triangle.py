# triangle

# http://www.lintcode.com/en/problem/triangle/

# state: 
# function:
# init: 
# answer: 

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    # # 1. traverse method: O(2^n)
    # best = float("inf")

    # def minimumTotal(self, triangle):
    #     self.traverse(triangle, 0, 0, 0)
    #     return self.best

    # def traverse(self, triangle, x, y, sum):
    #     n = len(triangle)
    #     if x == n:
    #         if sum < self.best:
    #             self.best = sum
    #         return
    #     self.traverse(triangle, x+1, y, sum+triangle[x][y])
    #     self.traverse(triangle, x+1, y+1, sum+triangle[x][y])

    # # 2. D&C method: O(2^n)
    # def minimumTotal(self, triangle):
    #     return self.divideConquer(triangle, 0, 0)

    # def divideConquer(self, triangle, x, y):
    #     n = len(triangle)
    #     # base case, the level under the lowest level - nothing
    #     if x == n:
    #         return 0
    #     # divide
    #     down = self.divideConquer(triangle, x+1, y)
    #     downright = self.divideConquer(triangle, x+1, y+1)
    #     # conquer
    #     return min(down+triangle[x][y], downright+triangle[x][y])

    # # 3. D&C + Memoization (global dict visited to record the computed results)
    # def minimumTotal(self, triangle):
    #     global visited
    #     visited = {}
    #     for i in xrange(len(triangle)):
    #         for j in xrange(len(triangle[i])):
    #             visited[i, j] = -1
    #     return self.divideConquer(triangle, 0, 0)

    # def divideConquer(self, triangle, x, y):
    #     n = len(triangle)
    #     # base case, the level under the lowest level - nothing
    #     if x == n:
    #         return 0
    #     # check memorized items
    #     if visited[x, y] != -1:
    #         return visited[x, y]
    #     # divide
    #     down = self.divideConquer(triangle, x+1, y)
    #     downright = self.divideConquer(triangle, x+1, y+1)
    #     # conquer
    #     visited[x, y] = min(down+triangle[x][y], downright+triangle[x][y])
    #     return visited[x, y]

    # # 4. Bottom-up DP
    # def minimumTotal(self, triangle):
    #     f = f = [[0 for item in triangle[nrow]] for nrow in xrange(len(triangle))]
    #     n = len(triangle)
    #     # init the bottom
    #     for j in xrange(len(triangle[n-1])):
    #         f[n-1][j] = triangle[n-1][j]
    #     # loop from the bottom row
    #     # note xrange(start, end, step), start inclusive, end exclusive
    #     for i in xrange(n-2, -1, -1):
    #         for j in xrange(len(triangle[i])):
    #             f[i][j] = min(f[i+1][j]+triangle[i][j], f[i+1][j+1]+triangle[i][j])

    #     return f[0][0]

    # 4. Top-down DP
    def minimumTotal(self, triangle):
        inf = float("inf")
        nrow = len(triangle)
        # init
        f = [[inf for j in xrange(i+1)] for i in xrange(nrow)]
        f[0][0] = triangle[0][0]
        # function
        # careful, i starts from 1, not 0, because f[i][j] += A[i][j] doesn't execute for f[0][0]
        for i in xrange(1, nrow):
            for j in xrange(i+1):
                # careful, f[i-1][j] exists condition: 0 <= j <= i-1
                if i - 1 >= 0 and 0 <= j <= i-1:
                    f[i][j] = min(f[i][j], f[i-1][j])
                if i - 1 >= 0 and 0 <= j - 1 <= i-1:
                    f[i][j] = min(f[i][j], f[i-1][j-1])
                f[i][j] += triangle[i][j]
        return min(f[-1]) 


Sol = Solution()
tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print Sol.minimumTotal(tri)
# print range(10, 0, -1)
# f = [[0 for item in tri[nrow]] for nrow in xrange(len(tri))]
# print f