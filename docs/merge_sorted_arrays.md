#### merge sorted arrays
>Given a list of `K` sorted arrays, combine them to output
a single merged sorted array, total `N` elements

This is directly from Elements of Programming Interviews in Python.
From the chapter on Heaps.

We keep the smallest element, also the first element, of each
sorted array in a min heap (`K` elements) and keep extracting the min every time
(`O(1)` time) and inserting the next element from that array, from
which the element was just popped (`O(logK)` time). We do this
for all the N elements, and so we complete this problem in 
`O(N * logK)` time and `O(K)` space.

A brute force would combine all the elements in a merged list and
then sort it, which completes this problem in O(N * logN) time.

The effectiveness of min-heap solution comes out when we have
N very larger than K. Like 3 sorted arrays of 1 million numbers
each.

This is my solution:
```python
import heapq


def merge_sorted_arrays(sorted_arrays):
    """
    Merge sorted arrays using a min-heap of the smallest entries
    in each remnant of the sorted arrays
    :param sorted_arrays: list of sorted arrays
    :return: a merged list of all sorted arrays
    """
    result = []

    # Build the min-heap using the first entries of each sorted array
    min_heap = [elem[0] for elem in sorted_arrays if elem != []]
    heapq.heapify(min_heap)

    # continue till the heap is empty
    while min_heap:
        # Pop the smallest element, call it popped
        popped = heapq.heappop(min_heap)
        # Find the array from which the element was popped
        index = [popped in elem for elem in sorted_arrays].index(True)
        # Remove the element from that array
        sorted_arrays[index].remove(popped)
        # If the array has remaining elements, push the first element in the heap
        if sorted_arrays[index]:
            heapq.heappush(min_heap, sorted_arrays[index][0])
        # Put the popped element in the result
        result.append(popped)

    return result
```

One of the problems with the above code is that for finding the array I am using
a list comprehension to search for the `popped` element, among the sorted arrays in
`sorted_arrays`. This takes `O(N)` time. So every time I am popping, I am doing a search
which takes `O(N)` time and also an insertion taking `O(logK)` time. Since `N>>K`, each
step is taking `O(N)` time. So at the end this is a `O(N^2)` solution. Bad.

What we can do is remember the arrays from which each number is coming to the heap. This
can be done using `enumerate`.

There is one more problem. `remove`, or `pop(0)` from list takes `O(N)` time complexity. We could keep a set of iterators in
memory corresponding to each sorted array in `sorted_arrays`.

This brings to EPI's solution:

```python
import heapq

def merge_sorted_arrays_epi(sorted_arrays):
    min_heap = []

    # Builds a list of iterators for each array in sorted_arrays:
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result
```

This takes some extra `O(K)` space but it's `O(N * log(K))` time solution.