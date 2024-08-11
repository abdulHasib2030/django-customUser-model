from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError("Users must have an email address.")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, name, password = None):
        user = self.create_user(
            email,
            name = name,
            password=password
        )

        user.is_admin = True
        user.save(using = self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name= 'Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

