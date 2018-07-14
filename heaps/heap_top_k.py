import itertools
import heapq
import unittest


# O(nlogk) algorithm to find the k largest strings from stream of strings
# Using a min-heap
def top_k(k, stream):
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream[k:]:
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nlargest(k, min_heap)]


class Test(unittest.TestCase):
    def test_top_k(self):
        stream = ["Hello", "World", "How", "Are", "You", "Computer", "Programming"]
        k = 5
        self.assertListEqual(top_k(k, stream), ['Programming', 'Computer', 'World', 'Hello', 'You'])
