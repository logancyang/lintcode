## Dynamic Programming

Dynamic programming has a broad vision for searching the optimal solution by memorizing the intermediate results. However, dynamic programming is quite abstract. It’s not an algorithm and it doesn’t have a template. It’s a methodology.

`Recursion/divide&conquer + memoization = DP`. 

The essence of DP is that it remembers the results of the subproblems to avoid repeated computation. More often, it takes the form of nested for loops, computing a array/matrix of subproblem results.

Here we take the triangle problem to show different methods.

### Method 1: Traverse

Traverse: pass “sum” in as a parameter. Need a global variable “best” to keep track of the optimal result across all recursions.

It has a time complexity of O(2^n), since each recursion level we have 2 choices.

```python
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    # traverse method: complexity O(2^n)
    best = float("inf")

    def minimumTotal(self, triangle):
        self.traverse(triangle, 0, 0, 0)
        return self.best

    def traverse(self, triangle, x, y, sum):
        n = len(triangle)
        if x == n:
            if sum < self.best:
                self.best = sum
            return
        self.traverse(triangle, x+1, y, sum+triangle[x][y])
        self.traverse(triangle, x+1, y+1, sum+triangle[x][y])
```

### Method 2. Divide & Conquer

Return “sum” from each recursion. Complexity is also O(2^n) since its recursion is the same as method 1. Only this time we return the result instead of passing it in as a parameter.

```python
    # D&C method: O(2^n)
    def minimumTotal(self, triangle):
        return self.divideConquer(triangle, 0, 0)

    def divideConquer(self, triangle, x, y):
        n = len(triangle)
        # base case, the level under the lowest level - nothing
        if x == n:
            return 0
        # divide
        down = self.divideConquer(triangle, x+1, y)
        downright = self.divideConquer(triangle, x+1, y+1)
        # conquer
        return min(down+triangle[x][y], downright+triangle[x][y])
```

The essence of the reason why DP is faster than method 1 and 2 for this problem is that there are only `N = n^2` nodes, but these 2 methods computed the intermediate results for the red nodes multiple times. We should record these results to avoid unnecessary computation, and here comes DP.

**When there’s repeated computation, we use DP.**

### Method 3. D&C + Memoization

We record which nodes we have already computed and store the results in a global dict “visited”. It’s global for the D&C method to see. If not computed, visited[x, y] = -1. This is basically DP thinking already, but there are better forms.

```python
    # 3. D&C + Memoization (global dict visited to record the computed results)
    def minimumTotal(self, triangle):
        global visited
        visited = {}
        for i in xrange(len(triangle)):
            for j in xrange(len(triangle[i])):
                visited[i, j] = -1
        return self.divideConquer(triangle, 0, 0)

    def divideConquer(self, triangle, x, y):
        n = len(triangle)
        # base case, the level under the lowest level - nothing
        if x == n:
            return 0
        # check memorized items
        if visited[x, y] != -1:
            return visited[x, y]
        # divide
        down = self.divideConquer(triangle, x+1, y)
        downright = self.divideConquer(triangle, x+1, y+1)
        # conquer
        visited[x, y] = min(down+triangle[x][y], downright+triangle[x][y])
        return visited[x, y]
```

I’d like to add some comment for computing the time complexity of recursions here. Some cases for recursion:
1. Subsets —> O(2^n), because for each element in a total of n elements, we can choose to include it or not.
2. Permutations —> O(n!)
3. Something like a tree: we check how many nodes there are, and how many times we visit each node, multiply the two.
	1) If it’s a binary tree with N nodes, visit each node once —> O(N)
	2) If it’s a “tree” like this triangle, we have n^2 nodes where n is # levels, though we visit each node multiple times but we only compute its result once.

### Method 4. Loop, the bottom-up approach

Complexity O(n^2). (A is the triangle)

```
State: f[i][j] = the min sum from node (i, j) to the bottom level
Function: f[i][j] = min(f[i+1][j]+A[i][j], f[i+1][j+1]+A[i][j])
Init: f[n-1][j] = A[n-1][j]
Result: f[0][0]
```
```python
    # 4. Bottom-up DP
    def minimumTotal(self, triangle):
        f = f = [[0 for item in triangle[nrow]] for nrow in xrange(len(triangle))]
        n = len(triangle)
        # init the bottom
        for j in xrange(len(triangle[n-1])):
            f[n-1][j] = triangle[n-1][j]
        # loop from the bottom row
        # note xrange(start, end, step), start inclusive, end exclusive
        for i in xrange(n-2, -1, -1):
            for j in xrange(len(triangle[i])):
                f[i][j] = min(f[i+1][j]+triangle[i][j], f[i+1][j+1]+triangle[i][j])

        return f[0][0]
```

### Method 5 (best): Loop, the top-down approach

Complexity O(n^2). We re-define the state. It’s different from the state in method 4.
```
State: f[i][j] = the min sum from node (0, 0) to (i, j)
Function: f[i][j] = min(f[i-1][j]+A[i][j], f[i-1][j-1]+A[i][j])
Init: f[0][0] = A[0][0]
Result: min(f[-1][j])
```
In this case, there are several pitfalls we need to pay special attention to.
1. Initialize the “empty” states to be inf. Because we are comparing and getting the min.
2. Start the i loop (row) from 1, as in most DP, since 0 is the initialized point.
3. It’s possible that the (i-1, j) or (i-1, j-1) node doesn’t exist. Check first. Pay special attention to the existence condition of j for the upper i-1 row.

```python
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
```


When do we use DP?

* Find max/min
* Yes/no: is there a solution for xxx or not
* Count the # solutions

When it’s probably not DP?

* Show all solutions, not # solutions. (For example, palindrome partitioning)
* Given a set, not a sequence. We need order to perform DP. (For example, longest consecutive sequence. Though it's called a sequence, it's not.)

How do we form a DP solution?

* Define the state, f. It's the hardest part of a DP problem, but most DP problems can be categorized into a few kinds: matrix DP (15%), sequence DP (40%), two-sequence DP (40%), others (5%).
* Find the function. From the connection of the states, find how to compute larger states from smaller ones.
* Initialization. Check what the base case is. Starting point.
* Answer. Check what the final case is. End point.

Triangle is a matrix DP problem.

## MATRIX DP

```
State: f[x][y], the cost of traveling from (0, 0) to (x, y)
Function: check the relationship between the current step and the previous step
Init: starting point, or 1st row, 1 col
Answer: end point f[-1][-1]
```

### Min Path Sum

```
category: min/max
matrix, can go down or right, find minPathSum
    state: f[x][y], min sum from (0, 0) to (x, y)
    function: f[x][y] = min(f[x-1][y], f[x][y-1]) + grid[x][y]
    init: f[0][0] = grid[0][0], f[i][0] = sum(grid[i][0], 0 -> i inclusive), f[0][j] = sum(grid[0][j], 0 -> j inclusive)
    answer: f[-1][-1]
```

### Unique Path

```
category: # solutions
matrix, can go down or right, find # path to the lower right corner
    state: f[x][y], # path from (0, 0) to (x, y)
    function: f[x][y] = f[x-1][y] + f[x][y-1])
    init: f[0][0] = 1 = f[0][j] = f[i][0]
    answer: f[-1][-1]
```

### Unique Path with Obstacles: 
* Check if start point is blocked, if yes, return 0.
* Check in the function if the current point is blocked.
* The function is the same as Unique Path I otherwise.

```
category: # solutions
matrix, can go down or right, find # path to the lower right corner. Check if start is an obstacle, if yes, return 0.
    state: f[x][y], # path from (0, 0) to (x, y)
    function: f[x][y] = f[x-1][y] + f[x][y-1] if not obstacle, 0 if yes
   *init: f[0][0] = 1 if not obstacle. f[0][j] = f[i][0] = 1 if no obstacle, all 0 after hitting an obstacle
    answer: f[-1][-1]
```

## SEQUENCE DP

```
State: f[i], the first i positions; ending at ith or starting at ith…
Function: f[i] = f[j]… j is before i
Init: f[0]…
Answer: f[-1]…
```

### Climbing Stairs

If there are 4 steps to climb: 
```
0th step: [(1)] —> 1
1st step: [(1, 1), (2)] —> 2
2nd step: [(1, 1, 1), (1, 2), (2, 1)] —> 3
3rd step: [(1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2)] —> 5
…
```
It’s a fibonacci sequence.

```
category: # solutions
    state: f[i], # ways from 0 to i
    function: f[i] = f[i-1] + f[i-2]
    init: f[0] = 1, f[1] = 2
    answer: f[n-1], since we count from 0
```

### Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

```
category: yes/no

    state: f[i], means I can reach the ith position or not (Bool)
    function: f[i] = any(j is reachable && j can jump to i, j < i). any() means any(True) -> True.

              j is reachable: f[j] = True
              j can jump to i: j + A[j] >= i
              in practice, this any() is done by setting True at the first encounter and break the j loop

    init: f[0] = True
    answer: f[n-1]

Remarks: to check a list of bools in Python, use all() == .. and any() == ..
```

For this problem, DP is not the best method: `O(n^2)`. 

*A greedy method is O(n):* 

Keep track of the rightmost index we can reach by comparing the previous rightmost with the current j + A[j], if rightmost exceeds the target, it’s a yes; if i reaches rightmost, and still no yes, it’s a no.

### Jump Game II

Find the min steps we can jump to the end.

```
category: min/max

    state: f[i], the min # steps from 0 to i
    function: f[i] = min(f[j] + 1, j < i && j can jump to i),
                j is reachable: f[j] != inf
                j can jump to i: j + A[j] >= i
    init: f[0] = 0
    answer: f[n-1]
```

One note: f is always increasing. We want the min f[i] = f[j] + 1 when we loop through j, we take advantage of the fact that f is increasing, once f[i] gets a value we can break the j loop. It’s guaranteed that the earliest f[j] is the smallest.

Again, just like Jump Game I, DP is not the best solution here. We have a two-pointers solution:

```python
    # 2-pointers: O(n)
    def jump2pointers(self, A):
        if A is None or len(A) == 0:
            return 0
        # bug
        # input: [0]
        # expect: 0
        if len(A) == 1:
            return 0
        n = len(A)
        start = 0
        end = 0
        steps = 0
        while end < n - 1:
            maxim = 0
            steps += 1
            for i in xrange(start, end+1):
                maxim = max(maxim, i + A[i])
                if maxim >= n - 1:
                    return steps
            start = end + 1
            end = maxim
            if start > end:
                break
        return float("inf")
```

### Palindrome Partitioning II

```
# Solution
State f[i]: min # cuts for the first i chars, s[:i] (i exclusive)
Function: f[i] = min(f[j]+1), j < i and s[j:i] isPalindrome. j -> 0:i
Init: f[i] = i-1, f[0] = -1
Answer: f[-1]

Remark:
f[i] —> s[:i], the first i chars
```

Loop i from 1 to n+1 exclusive, j from 0 to i exclusive.

### Word Break

```
yes/no
State f[i]: bool, can the first i chars be cut
Function: f[i] = any(f[j]), j < i, (j+1)th char to ith char is a word
Init: f[0] = True. For yes/no problems, f[0] = True
Answer: f[len(s)]

Optimization: word max length l, inner loop on l, check f[i-l] and s[i-l:i].
O(n^2) —> O(nl)

Remark:
Caution, f[i] -> s[:i], so f[i-l] -> s[:i-l], check s[i-l:i] at this time
```

Pay close attention to the loop bounds and the indices!
f init to length n+1, loop i from 1 to n+1 exclusive. For the unoptimized word break we loop j from 0 to i exclusive. For the word length optimized version we loop l from `1 to min(maxlen, i) + 1` exclusive.


## Two Sequence DP

### Longest Common Subsequence

```
min/max
State f[i][j]: first i chars in sequence a against first j chars in sequence b, the LCS length
Function: 
    # i-1 is now the ith char, because i loop 1 -> m+1 exclusive
    if a[i-1] == b[j-1]:
        f[i][j] = f[i-1][j-1] + 1
    else:
        f[i][j] = max(f[i-1][j], f[i][j-1])
Init: fdim = (len(a)+1, len(b)+1), f[i][0] = 0, f[0][j] = 0
Answer: f[-1][-1], or f[len(a)][len(b)]
```

Again, f[0][0] corresponds to no chars, we have to be careful about the correspondence between f and the string.
f[i][j] corresponds to A[i-1] and B[j-1].

### Longest Common Substring

```
min/max
State f[i][j]: the first i chars in A against the first j chars in B, the LCSubstring
Function:
    # i, j from 1 -> len+1 exclusive, meaning A[i-1] is the ith char
    if A[i-1] == B[j-1]:
        f[i][j] = f[i-1][j-1] + 1
    else:
        f[i][j] = 0
Init: f[i][0] = 0, f[0][j] = 0
Answer: max(f[][])
```

Similar to subsequence except the != case is 0 this time.

### Edit Distance

```
min/max
State f[i][j]: the min steps from the first i chars in word1 to the first j chars in word2
Function:
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
Init: f[0][j] = j, f[i][0] = i
Answer: f[-1][-1]
```

### Distinct Subsequences

```
count # solutions: # subsequences of S == T
State f[i][j]: the # solutions for the first i of S and the first j of T
Function: 
                if S[i-1] == T[j-1]:
                    f[i][j] = f[i-1][j] + f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j]
Init: f[i][0] = 1, f[0][j] = 0, j>0
Answer: f[-1][-1]
```

### Interleaving String

```
yes/no
State f[i][j]: can the first i chars in s1, and the first j chars in s2,
               interleave to produce the first i+j chars in s3
Function: 
        f[i][j] = (f[i-1][j] and s1[i-1] == s3[i+j-1]) or
                  (f[i][j-1] and s2[j-1] == s3[i+j-1])
        Comment: can the first i-1 chars of s1 and first j chars in s2 get
                 first i-1+j chars in s3, and in the case that, 
                 the ith char in s1 matches the (i+j)th char in s3.
                 Or,
                 ...
Init: f[i][0] = (s1[:i] == s3[:i]), f[0][j] = (s2[:j] == s3[:j])
Answer: f[-1][-1]

Remarks:
len(s3) = len(s1) + len(s2)
keep relative order in each string in the result string
```