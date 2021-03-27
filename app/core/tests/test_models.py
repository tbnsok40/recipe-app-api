from django.test import TestCase
from django.contrib.auth import get_user_model

# at some point, you may want to change what ur user model is and \
# if everything is using the get user model function then that's really easy to do.

# because you just change it in the settings instead of having to change all the ref to the user model.


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@douzone.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))

