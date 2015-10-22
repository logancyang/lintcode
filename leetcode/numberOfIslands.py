# numberOfIslands: https://leetcode.com/problems/number-of-islands/

"""
Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

# DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n, count = len(grid), len(grid[0]), 0
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and grid[i][j] == "1":
                    self.dfs(grid, visited, i, j, m, n)
                    count += 1
        return count

    def dfs(self, grid, visited, i, j, m, n):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited[i][j] = True
        for direction in dirs:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i < 0 or new_i >= m:
                continue
            if new_j < 0 or new_j >= n:
                continue
            if grid[new_i][new_j] != "1" or visited[new_i][new_j]:
                continue
            self.dfs(grid, visited, new_i, new_j, m, n)

# BFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n, count = len(grid), len(grid[0]), 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] != "1":
                    continue
                count += 1
                queue = [[i, j]]
                grid[i][j] = "2"
                while queue:
                    x, y = queue.pop(0)
                    for direction in dirs:
                        new_x = x + direction[0]
                        new_y = y + direction[1]
                        if new_x < 0 or new_x >= m:
                            continue
                        if new_y < 0 or new_y >= n:
                            continue
                        if grid[new_x][new_y] == "1":
                            grid[new_x][new_y] = "2"
                            queue.append([new_x, new_y])
        return count


