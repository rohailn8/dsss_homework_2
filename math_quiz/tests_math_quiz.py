import unittest
from math_quiz import generateRandomNumber, generateRandomOperator, calculatorFunction


class TestMathGame(unittest.TestCase):

    def test_generateRandomNumber_within_range(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateRandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    
    def test_generateRandomNumber_minimum_greater_than_maximum(self):
        # Test if minimum value is indeed smaller than maximum value
        min_val = 10
        max_val = 1
        with self.assertRaises(ValueError) as error:
            generateRandomNumber(min_val, max_val)
        self.assertEqual(str(error.exception), "minimumNumber should be less than maximumNumber")
    
    def test_generateRandomNumber_non_integer_inputs(self):
        # Test if values given are in the correct Integer format
        with self.assertRaises(ValueError) as error:
            generateRandomNumber(1.5, 10)  # minimumNumber as a float
        self.assertEqual(str(error.exception), "Both minimumNumber and maximumNumber should be an integer")

        with self.assertRaises(ValueError) as error:
            generateRandomNumber(1, "10")  # maximumNumber as a string
        self.assertEqual(str(error.exception), "Both minimumNumber and maximumNumber should be an integer")

        with self.assertRaises(ValueError) as error:
            generateRandomNumber("1", [10])  # minimumNumber as a string and maximumNumber as a list
        self.assertEqual(str(error.exception), "Both minimumNumber and maximumNumber should be an integer")
    
    def test_generateRandomOperator_format(self):
        operator = generateRandomOperator()
        self.assertIsInstance(operator, str)  # Check that the returned operator is a string
    
    def test_generateRandomOperator_validity(self):
        for _ in range(1000):
            operator = generateRandomOperator()
            self.assertIn(operator, ['+', '-', '*'])  # Check that the returned operator is a string
    
    def test_calculatorFunction(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '*', '6 * 3', 18),
                (9, 4, '+', '9 + 4', 13),
                (1, 6, '-', '1 - 6', -5)            
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Getting the calculated values from the calculator function
                problem, answer = calculatorFunction(num1, num2, operator)
                # Checking that the problem is same as expected problem
                self.assertEqual(problem, expected_problem)
                # Checking that the answer is same as expected answer
                self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
