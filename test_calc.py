import unittest
from calc import get_failure_probability, get_success_probability


class TestMeetingProbability(unittest.TestCase):
    def test_paper_example(self):
        # m=5, ℓ=40, r=20 should give ~28% failure, ~72% success
        fail_prob = get_failure_probability(5, 40, 20)
        success_prob = get_success_probability(5, 40, 20)
        self.assertAlmostEqual(fail_prob, 0.28, places=2)
        self.assertAlmostEqual(success_prob, 0.72, places=2)

    def test_guaranteed_success(self):
        # Not enough rejections to block all slots
        fail_prob = get_failure_probability(5, 40, 1)
        success_prob = get_success_probability(5, 40, 1)
        self.assertEqual(fail_prob, 0.0)
        self.assertEqual(success_prob, 1.0)

    def test_guaranteed_failure(self):
        # Everyone rejects everything
        fail_prob = get_failure_probability(5, 40, 41)
        success_prob = get_success_probability(5, 40, 41)
        self.assertEqual(fail_prob, 1.0)
        self.assertEqual(success_prob, 0.0)


if __name__ == "__main__":
    unittest.main()
