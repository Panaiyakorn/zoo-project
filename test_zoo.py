import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    # Test case: Child age (0-12)
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    # Test case: Teenager age (13-20)
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    # Test case: Adult age (21-60)
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  

    # Test case: Senior age (60+)
    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

    # Test case: Invalid age
    def test_invalid_age(self):
        self.assertIsNone(self.zoo.get_ticket_price(-1))  
        self.assertIsNone(self.zoo.get_ticket_price(-10)) 

if __name__ == '__main__':
    unittest.main()
