
### 1. Queue: BFS (must-master)


### 2. Stack: Min Stack

The idea is that we maintain 2 stacks, a target stack and a minStack. When we push an item in the target stack, we push the current min in the minStack. The min can be compared like this: min(number pushed in, top item in minStack). Each time we pop, we pop from minStack, too.


### 3. Stack: Queue by 2 Stacks

The trick lies in the function adjust(): only when stack2 is empty, pour things in from stack1. Do not push to stack2 if it¡¯s not empty, it will ruin the order. When we push, we push to stack1. We we top() or pop(), adjust first and get the result from stack2.


### 4. Stack: Largest Rectangle in Histogram

The brute force method is to enumerate the start point and the end point of a rectangle.

for i: start_of_rect:
	for j: end_of_rect:
		scan for min_height
		area = (j - i + 1) * min_height

A better method is to enumerate the lowest point of a rectangle.

for i is the lowest:
	find to the left the 1st piece lower than i, x
	find to the right the 1st piece lower than i, y
	area = (y - x + 1) * height[i]

When we want to search to the left/right for a 1st number that is smaller/bigger than the current number, we use stack.

For example, the sequence 2, 1, 5, 6, 2, 3, we want the 1st smaller number¡¯s index for each item.
(A: seq, I: index, S: stack. We store indices in I, the index of the 1st smaller number left to the current number. x means nothing.)

In this example, we want the first smaller number to the left and to the right. The stack works as the following: if current is smaller than stack top, pop the top out and push current in; if current is bigger than top, just push current in. So this stack is always increasing.

*To emphasize the point of using this stack: in this increasing stack, the item to the left of item i is i¡¯s 1st smaller to the left. And the item that kicks i out is i¡¯s 1st smaller to the right.*
```
i: 0 1 2 3 4 5
A: 2 1 5 6 2 3
S: 2
I: x
```
2 pushed in, S was empty, means 2 does not have a smaller number left to it.
```
A: 2 1 5 6 2 3
S: 1
I: x x
```
1 pushed in, pops out 2 because it¡¯s larger than 1, 1 has no smaller number left to it.
```
A: 2 1 5 6 2 3
S: 1 5
I: x x 1
```
5 pushed in, 1 is left to it, store 1¡¯s index for 5.
```
A: 2 1 5 6 2 3
S: 1 5 6
I: x x 1 2
```
6 pushed in, 5 is the 1st smaller number left to it. Store 5¡¯s index for 6.
```
A: 2 1 5 6 2 3
S: 1 2
I: x x 1 2 0
```
2 pushed in, pops out 6 and 5, check left, store 1¡¯s index for 2.
```
A: 2 1 5 6 2 3
S: 1 2 3
I: x x 1 2 0 4
```
3 pushed in, check left, store 2¡¯s index for 3.

For the 1st smaller number to the right, we can loop from the right to left.

A even better method with only one for loop is to catch the left smaller number and right smaller number at once. When a number gets popped out, its left smaller number is the stack top after the pop (or nothing if stack is empty after pop), its right smaller number is the current ith number, which kicked it out. So the width = i - stack_top - 1 (or i if stack empty), height = A[stack_popped].

Pay attention to one key point - this for loop computes one area for one popped item, so all items must get popped out. We add -1 at the end of the for loop so that all the items can be popped. For loop goes from 0 to len(A), not len(A) - 1.

This algorithm is O(n).

*When we want to search for the 1st smaller/bigger number to the left/right, use stack.*


### 5. Stack: Max Tree

Use the conclusion from the previous problem: find the first bigger number of an element to its left/right, with a stack.

In contrast to the previous problem, we want the first bigger instead of smaller, so the stack should pop top out when current is bigger than top. 

To determine the state of node i in max tree, we need it¡¯s parent, and whether it¡¯s a left child or a right child. We find the 1st bigger number to its left: x, and to its right: y, compare the two, if x < y, i is x¡¯s right child; if x > y, i is y¡¯s left child. Beware, i is the smaller number¡¯s child, not the bigger, since the bigger number is further up in the tree.

*To emphasize the point of using this stack: in this decreasing stack, the item to the left of item i is i¡¯s 1st bigger to the left. And the item that kicks i out is i¡¯s 1st bigger to the right.

At last, use inf to kick out all elements in stack, just like we used -1 in the previous problem. Because all searches for a node¡¯s 1st bigger to the left/right happen when a node is popped out.


### 6. Hash: APR Hash Function Magic Number 33

Two main points for this problem. First, in Python, use ord(¡°a¡±) to get ¡°a¡±¡¯s ascii. Second, for the equation,
```
hashcode("abcd") = (ascii(a) * 33^3 + ascii(b) * 33^2 + ascii(c) * 33 + ascii(d)) % HASH_SIZE
```
The % operation can be applied to each term in each iteration separately. So this equation can be convert to an iterative approach,
```
sum = 0
for char in string:
	sum = sum * 33 + ord(char)
	sum = sum % HASH_SIZE
return sum
```

*Hash table: open hashing and closed hashing.*

* Open hashing: hash chaining.
* Closed hashing: If slot occupied, fill the next slot.

In Java, Hashtable is thread-safe but slower than HashMap.


### 7. Hash: Rehashing*

The concept is in open hashing, when the number of elements is more than 1/10 of the capacity of the hash table, we double the capacity, and hash all element into the new hash table again. When hash collision, chain down.


### 8. Hash: Longest Consecutive Sequence

It¡¯s an quite straightforward idea. For each element in the list, we need to know how long it can stretch left and right consecutively - this is the outer for loop on all elements in list. 

Then for each iteration, we use 2 while loops to stretch right and left. If top (init at num[i]) / bottom (init at num[i] - 1) is in the hash_set (initialized to be all elements in list), increment/decrement by 1 and check again. DO NOT use set() as this hash_set, because it¡¯s not iterable and does not support the while loop checking in it, use a dict instead, it¡¯s iterable.

The length of the longest consecutive sequence for each element in list is (top - bottom - 1). For example in [4, 6, 7, 8, 9, 10, 12], for 8, top goes from 8 to 11 (not 10), bottom goes from 7 to 5 (not 6), top - bottom - 1 = 11 - 5 - 1 = 5. Notice the while loop stops when the number is NOT in the hash_set anymore.

The max(top - bottom - 1) for all iterations is the answer.


### 9. Hash: LRU Cache

LRU - Least Recently Used
(LFU - Least Frequently Used)

LinkedHashMap in Java can do this. Actually it¡¯s a doubly-linked (can be single-linked) list and a hash map.

When use the singly-linked list, hash[node.key] = prev. This achieved 2 points. 1st: we know what¡¯s the previous node of this node, just like calling node.prev in the doubly-linked list. Why do we need prev? Because when we delete node, we do prev.next = prev.next.next. 2nd: we can instantly look up node by going to its prev, and go to prev.next.

But singly-linked list is not very straightforward for thinking. If allowed, we can use doubly-linked list and make hash[node.key] = node. The other difference is that when we delete node, prev.next = node.next, node.next.prev = prev.

The methods for LRUCache are: __init__, push_back, pop_front, move_to_tail, get, set.
```
__init__(capacity): 
	init with capacity. Create hash = {}, head=Node(None), tail=head.

push_back(node): 
	set hash[node.key] = node; node.prev = tail, tail.next = node, new tail = node

pop_front():
	del hash[head.next.key], since head.next is the actual head, head is always dummy;
	delete the head.next node by setting dummy.next to its next¡¯s, and its next¡¯s prev to dummy

move_to_tail(node): (assumed node already in the list by context)
	if node is tail, return, do nothing;
	if not, del node in the doubly-linked list, and push_back(node)

get(key):
	if key not in our cache (hash), return -1;
	if key exists, move_to_tail(hash[key]), return hash[key].value

set(key, value):
	if key exists, move_to_tail, hash[key].value = value;
	if not, push_back(new_node(key, value)), if length exceed capacity, pop_front()
```

*Heap: Array, A[0] root, for A[i], left child is `A[i*2+1]`, right child is `A[i*2+2]`*
```
	push(): O(log N)
	pop(): O(log N)
	min() for min-heap, or max() for max-heap: O(1)
```
(The following examples are for min-heap)
For push(), append new node at the end, siftup() (swap with parent) if needed. If the new node is the min, it calls siftup() logN (height of the tree) times.

For pop(), swap the last node X with the target node. For X, if X is larger than any child, siftdown(X), meaning swap X with its smaller child (if we swap with the larger child, the larger child still needs siftdown()). We can pop() any node in the heap with the use of a hash map. Max time complexity still is the height, logN.

min() is O(1), A[0], the root.


### 10. Heap: Data Stream Median



### 11. Heap: Merge K Sorted Lists


### Heap: Heapify*

In heapofy(A), the big loop is the for loop starting from kth_node = len(A)/2, the lowest and last parent in the heap, call siftdown(A, kth_node), and decrement in each iteration.

Siftdown(A, k):

All of siftdown is this while loop. k can be the smallest already and break, or k can be updated to its child, `k * 2 + 1` or `k * 2 + 2`. Each iteration heapifies the current triangle, and pass to the its subtree triangle and check again.


### 12. Trie: Word Search II