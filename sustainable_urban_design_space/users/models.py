from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class User(User):
    first_name = None
    last_name = None
    