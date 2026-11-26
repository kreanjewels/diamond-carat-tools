import unittest
from decimal import Decimal, InvalidOperation
from carats import milligrams


class WeightTests(unittest.TestCase):
    def test_known_weights(self):
        for weight, expected in [("0", "0"), ("1", "200"), ("0.005", "1")]:
            with self.subTest(weight=weight):
                self.assertEqual(milligrams(weight), Decimal(expected))

    def test_invalid_weights(self):
        for weight in ["-1", "NaN", "Infinity", "abc"]:
            with self.subTest(weight=weight), self.assertRaises((ValueError, InvalidOperation)):
                milligrams(weight)
