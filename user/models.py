# from django.db import models, IntegrityError
# from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# import jwt
#
# class Role(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class UserManager(BaseUserManager):
#
#     def create_user(self, login, email, role, password):
#         if login is None:
#             raise TypeError('User must have a login')
#         if email is None:
#             raise TypeError('User must have an email')
#         if role is None:
#             raise IntegrityError('Role is required')
#
#         user = self.model(login=login,
#                           email=self.normalize_email(email),
#                           role=role)
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, login, email, role, password):
#
#         if password is None:
#             raise TypeError('Superuser must have a password')
#
#         user = self.create_user(login,email,role,password)
#         user.is_superuser = True
#         user.save()
#
#         return user
#
#
# class User(AbstractUser, PermissionsMixin):
#     name = models.CharField(max_length=150)
#     surname = models.CharField(max_length=150)
#     login = models.CharField(max_length=255, default=True, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     role = models.ForeignKey(Role, verbose_name='Role', on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     phone = models.IntegerField()
#
#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['email', 'role']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.login