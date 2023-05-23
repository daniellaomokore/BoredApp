import unittest
from unittest.mock import patch, MagicMock

from boredapp.boredAppFunctions import check_if_activity_is_in_favourites, is_user_logged_in, get_user_firstname, \
    get_user_id, check_if_strong_password


# The '@patch' decorator is used in this test case to replace the actual 'database','the_users' and 'datetime' module,
# in the main module with a mock object, created by the 'mock_database','mock_TheUser' and 'mock_datetime'  fixture.
class TestCheckIfActivityIsInFavourites(unittest.TestCase):
    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_check_if_activity_is_in_favourites_true(self, mock_query):
        # Set up the mock to return the expected value
        mock_query.return_value.filter_by.return_value.first.return_value = True

        # Call the function under test
        favouritesExists = check_if_activity_is_in_favourites(activityID=5, UserID=12)

        # Assert that the function returns True
        self.assertEqual(favouritesExists, True)

    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_check_if_activity_is_in_favourites_false(self, mock_query):
        # Set up the mock to return the expected value
        mock_query.return_value.filter_by.return_value.first.return_value = False

        # Call the function under test
        favouritesExists = check_if_activity_is_in_favourites(activityID=7, UserID=12)

        # Assert that the function returns False
        self.assertEqual(favouritesExists, False)


class TestIsUserLoggedIn(unittest.TestCase):
    # Test case for when a user is logged in
    @patch('boredapp.boredAppFunctions.session', {'UserID': 1})
    def test_user_logged_in(self):
        self.assertTrue(is_user_logged_in())  # Assert that the function returns True

    # Test case for when a user is not logged in
    @patch('boredapp.boredAppFunctions.session', {})
    def test_user_not_logged_in(self):
        self.assertFalse(is_user_logged_in())  # Assert that the function returns False


class TestGetUserFirstname(unittest.TestCase):
    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_firstname_with_email(self, mock_query):
        # create a mock user with a FirstName of "amy"
        mock_user = MagicMock()
        mock_user.FirstName = "amy"

        # create a mock session object
        mock_session = {'Email': 'test@example.com'}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = mock_user

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_firstname(), "Amy")

    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_firstname_with_username(self, mock_query):
        # create a mock user with a FirstName of "amy"
        mock_user = MagicMock()
        mock_user.FirstName = "bOB"

        # create a mock session object
        mock_session = {'Username': 'Gumball123'}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = mock_user

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_firstname(), "Bob")

    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_firstname_when_user_is_not_logged_in(self, mock_query):
        # create a mock session object
        mock_session = {'': ''}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = None

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_firstname(), "User is not logged in")


class TestGetUserID(unittest.TestCase):
    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_id_with_email(self, mock_query):
        # create a mock user with a UserID of "1526"
        mock_user = MagicMock()
        mock_user.UserID = 1526

        # create a mock session object
        mock_session = {'Email': 'test@example.com'}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = mock_user

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_id(), 1526)

    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_id_with_username(self, mock_query):
        # create a mock user with a UserID of "1111"
        mock_user = MagicMock()
        mock_user.UserID = 1111

        # create a mock session object
        mock_session = {'Username': 'Gumball123'}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = mock_user

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_id(), 1111)

    @patch('boredapp.boredAppFunctions.database.session.query')
    def test_get_user_id__when_user_is_not_logged_in(self, mock_query):
        # create a mock session object
        mock_session = {'': ''}

        # set the return value of the filter_by and first methods of the mock query object
        mock_query.return_value.filter_by.return_value.first.return_value = None

        # use the mock session object during the function call
        with patch('boredapp.boredAppFunctions.session', mock_session):
            self.assertEqual(get_user_id(), "User is not logged in")


class TestCheckIfStrongPassword(unittest.TestCase):
    def test_check_if_strong_password_is_false(self):
        weakPassword = "Bob"
        self.assertFalse(check_if_strong_password(weakPassword))

    def test_check_if_strong_password_is_true(self):
        strongPassword = "Bobiana123!"
        self.assertTrue(check_if_strong_password(strongPassword))


if __name__ == "__main__":
    unittest.main()
