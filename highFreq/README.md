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


