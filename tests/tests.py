import unittest
from ..app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Samuel", "test_password")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))


if __name__ == 'main':
    print('tests are running here')
    unittest.main()