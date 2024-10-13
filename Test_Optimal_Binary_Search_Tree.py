import unittest
from Optimal_Binary_Search_Tre import optimal_bst_cost


class TestOptimalBinarySearchTree(unittest.TestCase):

    def test_small_tree(self):
        keys = [10, 20, 30]
        freq = [3, 2, 4]
        expected_cost = 16
        expected_tree = (20, (10, None, None), (30, None, None))

        cost, tree = optimal_bst_cost(keys, freq, len(keys))
        self.assertEqual(cost, expected_cost)
        self.assertEqual(tree, expected_tree)

    def test_single_key(self):
        keys = [10]
        freq = [5]
        expected_cost = 5
        expected_tree = (10, None, None)

        cost, tree = optimal_bst_cost(keys, freq, len(keys))
        self.assertEqual(cost, expected_cost)
        self.assertEqual(tree, expected_tree)

    def test_empty_tree(self):
        keys = []
        freq = []
        expected_cost = 0
        expected_tree = None

        cost, tree = optimal_bst_cost(keys, freq, len(keys))
        self.assertEqual(cost, expected_cost)
        self.assertEqual(tree, expected_tree)

    def test_larger_tree(self):
        keys = [10, 20, 30, 40]
        freq = [4, 2, 6, 3]
        expected_cost = 26
        expected_tree = (30, (10, None, (20, None, None)), (40, None, None))

        cost, tree = optimal_bst_cost(keys, freq, len(keys))
        self.assertEqual(cost, expected_cost)
        self.assertEqual(tree, expected_tree)

    def test_non_consecutive_keys(self):
        keys = [5, 15, 25, 50]
        freq = [3, 1, 4, 2]
        expected_cost = 17
        expected_tree = (25, (5, None, (15, None, None)), (50, None, None))

        cost, tree = optimal_bst_cost(keys, freq, len(keys))
        self.assertEqual(cost, expected_cost)
        self.assertEqual(tree, expected_tree)


if __name__ == "__main__":
    unittest.main()
