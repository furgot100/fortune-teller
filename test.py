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




if __name__ == '__main__':
    unittest.main()