"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
import unittest


def flatten(l, answer=None):
    answer = answer or None
    for elem in l:
        if not isinstance(elem, list):
            answer.append(elem)
        else:
            flatten(elem, answer)
    return answer


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertListEqual(flatten([[[[[1, 2, 3, [[4, 5, [[6]]]], [7]]]]], [8, [[9]]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(flatten([[[[[[[[[[0]]]]]]]]]], answer=[]), [0])


if __name__ == "__main__":
    unittest.main()
