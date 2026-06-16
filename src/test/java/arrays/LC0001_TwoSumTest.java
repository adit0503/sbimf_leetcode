package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import java.util.Arrays;

class LC0001_TwoSumTest {

    private final LC0001_TwoSum solution = new LC0001_TwoSum();

    private void assertResult(int[] expected, int[] actual) {
        Arrays.sort(expected);
        Arrays.sort(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    void solution1_basicCase() {
        assertResult(new int[]{0, 1}, solution.solution1(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    void solution1_middleElements() {
        assertResult(new int[]{1, 2}, solution.solution1(new int[]{3, 2, 4}, 6));
    }

    @Test
    void solution1_duplicateValues() {
        assertResult(new int[]{0, 1}, solution.solution1(new int[]{3, 3}, 6));
    }

    @Test
    void solution2_basicCase() {
        assertResult(new int[]{0, 1}, solution.solution2(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    void solution2_middleElements() {
        assertResult(new int[]{1, 2}, solution.solution2(new int[]{3, 2, 4}, 6));
    }

    @Test
    void solution2_duplicateValues() {
        assertResult(new int[]{0, 1}, solution.solution2(new int[]{3, 3}, 6));
    }
}
