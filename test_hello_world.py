import hello_world
import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_result(self):
        result =self.app.get('/result')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()