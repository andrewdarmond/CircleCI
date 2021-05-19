from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that flask displays the landing page
    def test_landing(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Please fill out!' in response.data)

    def test_results(self):
        tester = app.test_client(self)
        response = tester.post('/result', follow_redirects=True)
        self.assertIn(b'Results', response.data)
    


if __name__ == '__main__':
    unittest.main()
