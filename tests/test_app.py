import unittest
from faker import Faker
from app import app

class TestAPI(unittest.TestCase): #inheriting testcase fuintionality from unittest

    def setUp(self):
        self.app = app.test_client()

    def test_sum(self): #stub test of the sum function, testing if function works with given data
        payload = {'num1': 3, 'num2': 5}
        response = self.app.post('/sum', json=payload) #sending post request to our apps /sum endpoint, awaiting a response
        data = response.json #getting the json data from the response
        self.assertEqual(data['result'], 8)

    def test_random_sum(self): #mocking a payload with random data
        fake = Faker()
        num1 = fake.random_number(digits=3)
        #num1 = fake.random_number(digits=3) #random number with 3 digits specified
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.json
        self.assertEqual(data['result'], num1 + num2)

if __name__ == '__main__':
    unittest.main() #runner for the test cases