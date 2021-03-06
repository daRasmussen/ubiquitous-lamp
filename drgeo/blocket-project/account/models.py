from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    """ REQUIRED """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
    This is the Account class hold info about the user account.
    """
    """ Custom Optional """
    image = models.ImageField(verbose_name='profile_image'),
    phone = models.CharField(max_length=30, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    about = models.TextField(max_length=300, default="")

    """ 
        TODO: 
        Address (include shipping as a param) ONE-to-MANY
        Billing                               ONE-to-MANY
        Items                                 ONE-to-MANY
    """

    """ Custom Required """
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)

    """ Required """
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Login field
    REQUIRED_FIELDS = ['username']  # required field to register

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.email}:{self.username}"

    """ REQUIRED FUNCTIONS """

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        return True
