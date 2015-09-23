### High Frequency Questions

#### Single Number

Key word: xor, binary addition without advancing digit, e.g.

```
01      0
01      1
---     ---
00      1
```

```python
n = n ^ A[i]
```

Then the final n is the single number which did not get cancelled out.


#### Single Number II

Key word: a self-defined operation, ternary addition without advancing digit, e.g.

```
012
012
012
---
000
```

Since our addition for the base3 numbers is without advancing digit, we can treat each bit of the base3
number separately. **Use a list** `bits` **of length 20 to store each bit, and loop over the 20 bits of each number.**
For each bit `i`, compute the digit for that bit, namely `A[j] / 3^i`) for all numbers, and accumulate at that bit.
The result of this accumulation is almost the "base3" form of the final result. We only need to `% 3` one more time
for each bit, and convert to decimal.

In this process, the operation that cancels to 0 when there is a triple is actually the accumulation at each bit and
modulo 3, in other words, the ternary addition without advancing digit.


#### Single Number III

Every number appears twice except two, a and b (which appear once). Then we wonder if we can separate the list into two groups,
so that each contains a or b, and we can use single number I's method to find a and b.

For `c = a ^ b != 0`, the binary form of c must have a digit which is not 0. Given the definition of XOR, the bit that's not
0 is where that bit of a and b are not equal. If we find that bit, separate all numbers according to that bit, the right groups are found.

There is a trick finding the bit that's 1 without looping through all bits. This trick is also used for telling if a number
is a power of 2 in O(1): if x is a power of 2, `x & (x - 1) = 0`.

For example, if x = 100000, x - 1 = 011111. 
```
    100000
AND 011111
-----------
    000000
```
If x = 10010, x - 1 = 10001
```
    10010
AND 10001
---------
    10000
```
`x - (x & (x - 1))` gives the last bit that's 1, e.g. `10010 - 10000 = 10`.

BUG: - has higher priority than &, add () around &


#### Majority Number

Find the majority number in the list: **we know it appears more than N/2 times**.

If we have 2 different numbers a and b, we accumulate both, and throw away one of each, at the end the one occurs more
will remain. This is the basic idea of this problem.

We set a `candidate` and accumulate its count, if we see a new number, we decrement candidate's count. If the count reaches 0, 
we have a new candidate. One pass and the remained candidate is the majority number.

Note that the majority number in this algorithm must occur more than N/2 times, or it won't work!


#### Majority Number II

The majority number in this question occurs more than N/3 times, and there is only one.

Use two candidates and two counts. Loop over the list, if the current number is `candidate1`, increment `count1`; 
if the current is `candidate2`, increment `count2`; else decrement both `count1` and `count2`.

Be careful, do not assume at the end that the larger of `count1` and `count2` is the majority number. Because the actual 
majority number's count can be cancelled at early stage, e.g. [1, 1, 4, 5, 1, 1, 6, 7, 8, 8], we may think 8 is the majority since 
1 gets cancelled out earlier.

BUG: DO NOT check `count1/2 == 0` first, instead, check `number == candidate1/2` first. **THE ORDER of `if, elif` MATTERS!**
For example, for `[1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4]`, if we check `count1/2 == 0` first, the first 1 gets assigned to 
`candidate1`, and the second 1 is assigned to `candidate2`, which will cause that `count1` can only reach 3 but not 4, so afterwards 
`count1` gets cancelled to 0 and `candidate1` will be assigned to 4, the real answer 1 is lost completely.


#### Majority Number III (Hash)

The idea is similar to Major Number I and II, we accumulate the count for each candidate. When the number of candidates (keys)
exceeds k, we remove (some) candidate(s) by the following procedure: one pass, decrement all counts; one pass, `del` the ones 
with 0 count. Note that do not delete element while iterating through the dict, record which ones to delete and delete them
in the next pass.

Then the next step is to re-count all counts for remaining candidates, and get the number with maximum count.

*Note: for a function with a dict passed in, del element from the dict inside the function is also modifying it globally. 
The case that the modification inside a function doesn't go out is when we use "=" inside a function instead of a method 
which the object has to modify itself.*


#### Maximum Subarray Sum

*Foreword: we must have negatives in the array to discuss this problem. If all positive, the subarray
would be itself and the problem is trivial.*

When there's something about subarray sum, think about *prefix sum*. The *prefix sum* of `i` is 
defined as the sum from index 0 to `i`, namely `prefix_sum[i] = sum(A[:i+1])`. Then if we need the 
subarray sum from `i` to `j`, we have `sub_sum_ij = prefix_sum[j] - prefix_sum[i-1]`.

Note that **we don't have to explicitly compute the prefix sums, it requires O(N^2)**. We only need an
accumulator. For item `j`, its accumulator not only gives us `prefix_sum[j]` which is simply the 
accumulator itself, we can also record its historical `min_sum`, the min prefix_sum before the 
current item `j`. This requires only one pass to yield the `max_diff` between `prefix_sum[j]` and 
its previous min `prefix_sum`. 

Beware,

* `min_sum` is initialized to 0, not +inf. Because it's actually a previous state of the accumulator,
and the accumulator starts at 0. For example, if the sum of `nums[:j]` (accumulator) reaches 0 or negative, 
`min_sum` is reset to 0.
* `max_diff` is the difference between prefix_sum elements, not the elements in the original 
array (**Best Time to Buy and Sell Stock**).

The prefix sum idea is a bit like *dynamic programming* in the sense that it avoid explicitly 
computing it, but update base on the previous iteration.


#### Best Time to Buy and Sell Stock

1 transaction, find `max_profit`. Similar to finding `max_diff` in Maximum Subarray Sum in the sense 
that it's one pass, but different because this one calculates the `max_diff` on this same array rather 
than the accumulator.

Iterate over all selling points, find the previous smallest number to be the buying point, so that 
`sell - buy` is maximum.

Set global max to 0, current min to `prices[0]`, 2 steps in the for loop:

* Find the current min value
* Find the global max by `max(global, local)`, where `local = prices[i] - current_min`

This idea is also used for a lot of questions, such as **Largest Rectangle in Histogram** and 
**Triangle** (min sum path). In the former, we enumerate the bars and check if we use it as the 
lowest in the rectangle, what the max area of that rectangle is. For the latter, we enumerate the 
min sum from the top to each end point, and find the min.


#### Best Time to Buy and Sell Stock II

Unlimited transactions. Cannot buy and sell at the same time, must sell after buying.

Greedy method. Any time there's a positive difference, add to profit.


#### Maximum Subarray Sum II

Similar to *Stock III*, but the scan from the right is the same as from the left in this case:

* `accumulator = 0, minSum = 0, max_diff = -inf`
* For loop from 0 (left) or from n-1 (right).
* `max_diff = max(max_diff, accumulator - minSum)`
* `minSum = min(minSum, accumulator)`
* Assign `left[i]` or `right[i]` to `max_diff` after.
* Note `left[i] + right[i+1]`.


#### Best Time to Buy and Sell Stock III

2 transactions. Similar to Maximum Subarray Sum II.

Split the array into 2 parts, and call the method of *Stock I* to compute the two max profits for left
and right portions. Then enumerate all split points, find the max sum for left and right.

The method above is the logical generalization of *Stock I*. But it has some redundant computations by calling
the method again and again, losing the `curr_min` and loop from the beginning when actually one pass can do the job.

So we implement the two parts of *Stock I* again in a more efficient way: save max profit for the left/right part in
list `left` / `right`, and combine them to give the 2-transaction sum. The corner cases: left or right part is empty.
When this happens, the max profit for that empty part is 0, and there is only 1 transaction.

Beware,

* `curr_min = prices[0]`, the scan from left to right: `local = prices[i] - curr_min`.
* `curr_max = prices[-1]`, the scan from right to left: `local = curr_max - prices[i]`.
* From left to right, index `range(1, n)`, because we have `left[i-1]`.
* From right to left, index `range(n-2, -1, -1)`, because we have `right[i+1]`.

#### Best Time to Buy and Sell Stock IV*

The solution is in directory *hard*.

#### Minimum Subarray

Find the minimum subarray sum. Instead, we can find maximum subarray for -A, and return `-max_diff`.

#### Maximum Subarray Difference

Find `|sum(A) - sum(B)|` for part A and B in the array.

The idea is to make `sum(A)` small and `sum(B)` big, or the opposite. It's the combination of **minSubarray**
and **maxSubarrayII**. Scan left and right,

* `left_small, right_big`, find max(diff) between the two lists.
* `left_big, right_small, find max(diff) between the two lists.
* Note that left[i] operates with right[i+1]!




















