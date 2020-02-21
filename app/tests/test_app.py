import unittest
import sys
sys.path.append(app/)

from flask_app import app

class TestCases(unittest.TestCase):
        def test_home(self):
                tester = app.test_client(self)
                response = tester.get('/v', content_type='html/text')
                self.assertEqual(response.status_code, 200)

        def test_other(self):
                tester = app.test_client(self)
                response = tester.get('a', content_type='html/text')
                self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


