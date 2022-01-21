import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        method to run before each test case.
        '''
        self.new_user = User("moha","hdx58")

    def tearDown(self):
        '''
        method to run after each test case.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"moha")
        self.assertEqual(self.new_user.password,"hdx58")

    def test_save_user(self):
        '''
         test to check if user is saved into user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
        
    def test_user_verification(self):
        self.new_user.save_user()
        user_confirm = User("moha", "hdx75")
        user_confirm.save_user()

        credential_found = User.user_verification("moha","hdx58")
        self.assertEqual(credential_found.username, user_confirm.username)
        

if __name__ == '__main__':
    unittest.main()