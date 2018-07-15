import heapq
import unittest


def merge_sorted_arrays(sorted_arrays):
    """
    Merge sorted arrays using a min-heap of the smallest entries
    in each remnant of the sorted arrays
    :param sorted_arrays: list of sorted arrays
    :return: a merged list of all sorted arrays
    """
    result = []

    # Build the min-heap using the first entries of each sorted array
    min_heap = [(elem[0], i) for (i, elem) in enumerate(sorted_arrays) if elem != []]
    heapq.heapify(min_heap)

    # continue till the heap is empty
    while min_heap:
        # Pop the smallest element, call it popped
        popped, array_i = heapq.heappop(min_heap)
        # Remove the element from that array
        sorted_arrays[array_i].pop(0)
        # If the array has remaining elements, push the first element in the heap
        if sorted_arrays[array_i]:
            heapq.heappush(min_heap, (sorted_arrays[array_i][0], array_i))
        # Put the popped element in the result
        result.append(popped)

    return result


def merge_sorted_arrays_epi(sorted_arrays):
    """
    EPI solution to merge_sorted_arrays
    using iterators & enumerate
    :param sorted_arrays:
    :return:
    """
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


def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


class Test(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertListEqual(merge_sorted_arrays([[], [1], [3, 5, 7], [2], [3], [3, 6, 7], [1, 4, 7, 8], []]),
                             [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8])
        self.assertListEqual(merge_sorted_arrays([[1], [2], [1], [], [3]]), [1, 1, 2, 3])

    def test_merge_sorted_arrays_epi(self):
        self.assertListEqual(merge_sorted_arrays_epi([[], [1], [3, 5, 7], [2], [3], [3, 6, 7], [1, 4, 7, 8], []]),
                             [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8])
        self.assertListEqual(merge_sorted_arrays_epi([[1], [2], [1], [], [3]]), [1, 1, 2, 3])

    def test_merge_sorted_arrays_pythonic(self):
        self.assertListEqual(merge_sorted_arrays_pythonic([[], [1], [3, 5, 7], [2], [3], [3, 6, 7], [1, 4, 7, 8], []]),
                             [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8])
        self.assertListEqual(merge_sorted_arrays_pythonic([[1], [2], [1], [], [3]]), [1, 1, 2, 3])