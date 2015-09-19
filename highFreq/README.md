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
number separately. Use a list `bits` of length 20 to store each bit, and loop over the 20 bits of each number.
For each bit `i`, compute the digit for that bit, namely `A[j] / 3^i`) for all numbers, and accumulate at that bit.
The result of this accumulation is almost the "base3" form of the final result. We only need to `% 3` one more time
for each bit, and convert to decimal.

In this process, the operation that cancels to 0 when there is a triple is actually the accumulation at each bit and
modulo 3, in other words, the ternary addition without advancing digit.


#### Single Number III


#### Single Number II

