import unittest

from backtracking.n_2375_construct_smallest_number_from_di_string import (
    ConstructSmallestNumberFromDIString,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        pattern = "IIIDIDDD"
        expected = "123549876"
        self.assertEqual(
            expected, ConstructSmallestNumberFromDIString.bruteforce_solution(pattern)
        )  # add assertion here

    def test_case_two(self):
        pattern = "DDD"
        expected = "4321"
        self.assertEqual(
            expected, ConstructSmallestNumberFromDIString.bruteforce_solution(pattern)
        )


if __name__ == "__main__":
    unittest.main()
