from django.db import models
# Create your models here.

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission

# validate iran national id
def validate_iran_national_id(value):
    code = str(value).strip()
    if not code.isdigit() or len(code) != 10:
        raise ValidationError("کد ملی باید دقیقا 10 رقم عددی باشد.")
    if len(set(code)) == 1:
        raise ValidationError("کد ملی نامعتبر است.")
    check = int(code[9])
    total = sum(int(code[i]) * (10 - i) for i in range(9))
    r = total % 11
    if (r < 2 and check != r) or (r >= 2 and check != (11 - r)):
        raise ValidationError("کد ملی نامعتبر است.")

# CustomUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, id_code, password=None, **extra_fields):
        if not id_code:
            raise ValueError("کد ملی نمی‌تواند خالی باشد.")
        id_code = str(id_code).strip()
        user = self.model(id_code=id_code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_code, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(id_code, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin):
    id_code = models.CharField(
        max_length=10,
        unique=True,
        validators=[validate_iran_national_id],
        verbose_name="کد ملی"
    )
    email = models.EmailField(
        verbose_name="ایمیل",
        blank=True,
        null=True,
        unique=True
    )
    image = models.ImageField(
        upload_to='users/',
        verbose_name="تصویر پروفایل",
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'id_code'  
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
    )

    def __str__(self):
        return f"{self.id_code} - {self.email or 'بدون ایمیل'}"
