import unittest

# A testcase is created by subclassing unittest.TestCase.
from src.BonusCalculator import BonusCalculator, InvalidTaxException, InvalidCommissionException


class BonusCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.bonus_calculator = BonusCalculator()

    #tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.
    def test_nobonus_when_sales_less_than_quota(self):
        result = self.bonus_calculator.calulate_bonus(12000, 15000, 10, 10)
        self.assertEqual(0, result)

    def test_nobonus_when_sales_equals_quota(self):
        result = self.bonus_calculator.calulate_bonus(12000, 12000, 10, 10)
        self.assertEqual(0, result)

    def test_bonus_when_sales_grater_then_quota(self):
        result = self.bonus_calculator.calulate_bonus(12000, 11000, 10, 10)
        self.assertEqual(90, result)

    def test_tax_should_be_less_or_equal_than_100(self):
        self.assertRaises(InvalidTaxException, self.bonus_calculator.calulate_bonus, 12000, 11000, 10, 101)

    def test_tax_should_be_grater_or_equal_than_(self):
        self.assertRaises(InvalidTaxException, self.bonus_calculator.calulate_bonus, 12000, 11000, 10, -1)

    def test_commission_should_be_less_or_equal_100(self):
        self.assertRaises(InvalidCommissionException, self.bonus_calculator.calulate_bonus, 12000, 11000, 101, 10)

    def test_commission_should_be_grater_or_equal_0(self):
        self.assertRaises(InvalidCommissionException, self.bonus_calculator.calulate_bonus, 12000, 11000, -1, 10)


if __name__ == '__main__':
    unittest.main()
