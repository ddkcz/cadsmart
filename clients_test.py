import unittest
import pandas as pd
import os

class TestClientDataGathering(unittest.TestCase):

    def test_happy_path(self):
        # Provide valid inputs
        input_values = ['John Doe', 'john@example.com', 'Personal', 'Client', 'Regular']
        with self.subTest(input_values=input_values):
            self.assertTrue(self.run_data_gathering(input_values))

    def test_multiple_iterations(self):
        # Test with qty > 1
        input_values_list = [
            ['John Doe', 'john@example.com', 'Personal', 'Client', 'Regular'],
            ['Alice Smith', 'alice@example.com', 'Business', 'Customer', 'VIP']
        ]
        for input_values in input_values_list:
            with self.subTest(input_values=input_values):
                self.assertTrue(self.run_data_gathering(input_values))

    def test_invalid_input_handling(self):
        # Provide invalid inputs
        input_values = ['John Doe', 'john@example.com', 'Personal', 123, 'Regular']
        with self.subTest(input_values=input_values):
            self.assertFalse(self.run_data_gathering(input_values))

    def test_csv_file_output(self):
        # Run the code and check if the CSV file is created
        csv_file_path = 'clients.csv'
        self.run_data_gathering(['John Doe', 'john@example.com', 'Personal', 'Client', 'Regular'])
        self.assertTrue(os.path.exists(csv_file_path))
        # Optionally, check if the CSV file contains the expected data

    def run_data_gathering(self, input_values):
        # Mock user input for testing
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            # Run data_gathering function
            data_gathering()
        # Optionally, return True if the function was successful or check other conditions
        return True

if __name__ == '__main__':
    unittest.main()