from django.test import TestCase
from django.contrib.auth import get_user_model


# at some point, you may want to change what ur user model is and \
# if everything is using the get user model function then that's really easy to do.

# because you just change it in the settings instead of having to change all the ref to the user model.


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@douzone.com'
        password = 'testpassword123'

        # create_user()메서드는 models.py에서 가져온 것..? ㄴㄴ get_user_model()에서 가져옴
        user = get_user_model().objects_.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@LONDON.COM'
        user = get_user_model().objects_.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())  # 양쪽 모두 소문자여야 test success

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):  # valueError가 일어나지 않으면 fail 한다.
            get_user_model().objects_.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects_.create_superuser(
            'test@name.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
# settings.py에서 AUTH_USER_MODEL = "core.User" 이렇게 설정을 해뒀기 때문에,
# get_user_model().objects_는 models.py의 class User()로 부터 온 것
