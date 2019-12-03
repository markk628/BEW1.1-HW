from app import app
import unittest 

class AppTests(unittest.TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_homepage(self):
        """Verify that homepage renders correctly."""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_fortune_result(self):
        result = self.app.get('/fortune_results?name=&siblings=&beverage_list=fortnite_shield&animal=dog')
        self.assertIn("{'stop playing fortnite you 12 year old', 'Your dog is cooler than you', ''}", str(result.data))

if __name__ == "__main__":
    unittest.main()

