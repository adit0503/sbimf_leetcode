import pytest
from solutions.arrays.lc0001_two_sum import Solution


@pytest.fixture
def sol():
    return Solution()


class TestTwoSumsolution:

    def test_basic_case(self, sol):
        assert sol.solution([2, 7, 11, 15], 9) == [0, 1]

    def test_middle_elements(self, sol):
        assert sol.solution([3, 2, 4], 6) == [1, 2]

    def test_same_elements(self, sol):
        assert sol.solution([3, 3], 6) == [0, 1]

    def test_negative_numbers(self, sol):
        assert sol.solution([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_large_array(self, sol):
        nums = list(range(1, 10001))
        assert sol.solution(nums, 19999) == [9998, 9999]
