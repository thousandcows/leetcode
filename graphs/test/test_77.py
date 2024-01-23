import unittest

from graphs.n_77_combinations import Combinations


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 4
        k = 2
        expected = [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
        self.assertEqual(
            sorted(expected), sorted(Combinations.solution(n, k))
        )  # add assertion here

    def test_case_two(self):
        n = 1
        k = 1
        expected = [[1]]
        self.assertEqual(expected, sorted(Combinations.solution(n, k)))

    def test_case_three(self):
        n = 2
        k = 1
        expected = [[1], [2]]
        self.assertEqual(expected, sorted(Combinations.solution(n, k)))

    def test_case_four(self):
        n = 20
        k = 2
        expected = [
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [3, 4],
            [3, 5],
            [3, 6],
            [3, 7],
            [3, 8],
            [3, 9],
            [3, 10],
            [3, 11],
            [3, 12],
            [3, 13],
            [3, 14],
            [3, 15],
            [3, 16],
            [3, 17],
            [3, 18],
            [3, 19],
            [3, 20],
            [4, 5],
            [4, 6],
            [4, 7],
            [4, 8],
            [4, 9],
            [4, 10],
            [4, 11],
            [4, 12],
            [4, 13],
            [4, 14],
            [4, 15],
            [4, 16],
            [4, 17],
            [4, 18],
            [4, 19],
            [4, 20],
            [5, 6],
            [5, 7],
            [5, 8],
            [5, 9],
            [5, 10],
            [5, 11],
            [5, 12],
            [5, 13],
            [5, 14],
            [5, 15],
            [5, 16],
            [5, 17],
            [5, 18],
            [5, 19],
            [5, 20],
            [6, 7],
            [6, 8],
            [6, 9],
            [6, 10],
            [6, 11],
            [6, 12],
            [6, 13],
            [6, 14],
            [6, 15],
            [6, 16],
            [6, 17],
            [6, 18],
            [6, 19],
            [6, 20],
            [7, 8],
            [7, 9],
            [7, 10],
            [7, 11],
            [7, 12],
            [7, 13],
            [7, 14],
            [7, 15],
            [7, 16],
            [7, 17],
            [7, 18],
            [7, 19],
            [7, 20],
            [8, 9],
            [8, 10],
            [8, 11],
            [8, 12],
            [8, 13],
            [8, 14],
            [8, 15],
            [8, 16],
            [8, 17],
            [8, 18],
            [8, 19],
            [8, 20],
            [9, 10],
            [9, 11],
            [9, 12],
            [9, 13],
            [9, 14],
            [9, 15],
            [9, 16],
            [9, 17],
            [9, 18],
            [9, 19],
            [9, 20],
            [10, 11],
            [10, 12],
            [10, 13],
            [10, 14],
            [10, 15],
            [10, 16],
            [10, 17],
            [10, 18],
            [10, 19],
            [10, 20],
            [11, 12],
            [11, 13],
            [11, 14],
            [11, 15],
            [11, 16],
            [11, 17],
            [11, 18],
            [11, 19],
            [11, 20],
            [12, 13],
            [12, 14],
            [12, 15],
            [12, 16],
            [12, 17],
            [12, 18],
            [12, 19],
            [12, 20],
            [13, 14],
            [13, 15],
            [13, 16],
            [13, 17],
            [13, 18],
            [13, 19],
            [13, 20],
            [14, 15],
            [14, 16],
            [14, 17],
            [14, 18],
            [14, 19],
            [14, 20],
            [15, 16],
            [15, 17],
            [15, 18],
            [15, 19],
            [15, 20],
            [16, 17],
            [16, 18],
            [16, 19],
            [16, 20],
            [17, 18],
            [17, 19],
            [17, 20],
            [18, 19],
            [18, 20],
            [19, 20],
        ]
        self.assertEqual(expected, sorted(Combinations.solution(n, k)))


if __name__ == "__main__":
    unittest.main()
