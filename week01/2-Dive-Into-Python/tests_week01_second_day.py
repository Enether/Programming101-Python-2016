import unittest
from solution import (count_substrings, sum_matrix, nan_expand, prime_factorization,
                      group, max_consecutive)


class Week02SecondDayTests(unittest.TestCase):

    def test_count_substrings(self):
        self.assertEqual(count_substrings("babababa", "baba"), 2)
        self.assertEqual(count_substrings("What what wHat what WwhAtwwhattt", "what"), 3)
        self.assertEqual(count_substrings('', ''), 1)

    def test_sum_numbers_in_matrix(self):
        self.assertEqual(sum_matrix([
            [1,1,1],
            [0,0,0],
            [0,0,0],
            [1],
            [1]]
        ), 5)

        self.assertEqual(sum_matrix([[1,2,3,4,5,6,7,8,9,11111111111,1]]), 11111111157)

        self.assertEqual(sum_matrix([[0,0,0], [-1, -1, -1], [1, 1, 1]]), 0)

        self.assertEqual(sum_matrix([[9223372036854775807, -9223372036854775807]]), 0)

    def test_NaN_expand(self):
        self.assertEqual(nan_expand(0), '')
        self.assertEqual(nan_expand(-1), '')
        self.assertEqual(nan_expand(5), 'Not a Not a Not a Not a Not a NaN')

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(1), [])
        self.assertEqual(prime_factorization(54154), [(2, 1), (27077, 1)])
        self.assertEqual(prime_factorization(54151), [(54151, 1)])
        self.assertEqual(prime_factorization(50), [(2, 1), (5, 2)])

    def test_group(self):
        self.assertEqual(group([1,1,1,'1',1,2,1,1]), [[1,1,1], ['1'], [1], [2], [1,1]])
        self.assertEqual(group([1,2,'3',4,5,5,2,5]), [[1], [2], ['3'], [4], [5,5], [2], [5]])
        self.assertEqual(group([]), [])
        self.assertEqual(group([[],[],[], {}, {}, {'the': "bad test"}, {'the': "bad test"}]),
                         [[[], [], []], [{}, {}], [{'the': "bad test"}, {'the': "bad test"}]])

    def test_longest_subsequence_of_equal_consecutive_elements(self):
        self.assertEqual(max_consecutive([1]), 1)
        self.assertEqual(max_consecutive([]), 0)
        self.assertEqual(max_consecutive([]), 0)
        self.assertEqual(max_consecutive([1, 1, '1', '1', '1', [], [], [], [], set(), set(), set(), set(), set(), set('d')]), 5)

if __name__ == "__main__":
    unittest.main()
