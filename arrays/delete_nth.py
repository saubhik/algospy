"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""
import unittest
from collections import defaultdict


def delete_nth(lst, N):
    hashmap = defaultdict(int)
    answer = []
    for num in lst:
        hashmap[num] += 1
        if hashmap[num] > N:
            break
        answer.append(num)
    return answer


class TestDeleteNth(unittest.TestCase):

    def test_delete_nth(self):
        self.assertListEqual(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2), [1, 2, 3, 1, 2])
        self.assertListEqual(delete_nth([], 5), [])


if __name__ == "__main__":
    unittest.main()
