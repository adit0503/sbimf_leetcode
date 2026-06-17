from solutions.arrays.lc0001_two_sum import Solution

s = Solution()


class TestSolution1:

    def test_basic(self):
        assert sorted(s.solution1([2, 7, 11, 15], 9)) == [0, 1]

    def test_middle_elements(self):
        assert sorted(s.solution1([3, 2, 4], 6)) == [1, 2]

    def test_duplicates(self):
        assert sorted(s.solution1([3, 3], 6)) == [0, 1]


class TestSolution2:

    def test_basic(self):
        assert sorted(s.solution2([2, 7, 11, 15], 9)) == [0, 1]

    def test_middle_elements(self):
        assert sorted(s.solution2([3, 2, 4], 6)) == [1, 2]

    def test_duplicates(self):
        assert sorted(s.solution2([3, 3], 6)) == [0, 1]
