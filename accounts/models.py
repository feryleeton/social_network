from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model"""

    email = models.EmailField('Email адреса', unique=True)
    username = models.CharField('Нікнейм', max_length=60, unique=True)
    first_name = models.CharField("Ім'я", max_length=255)
    last_name = models.CharField('Прізвище', max_length=255)
    date_joined = models.DateTimeField('Дата реєстрації', auto_now_add=True)
    is_active = models.BooleanField('Активний', default=True)
    last_activity = models.DateTimeField('Остання активність', auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", primary_key=True, verbose_name='Користувач')

    avatar = models.ImageField(upload_to='user_avatars/', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], blank=True, verbose_name='Аватар')

    # LOCATION INFO
    country = models.CharField(max_length=255, blank=True, verbose_name='Країна')
    city = models.CharField(max_length=255, blank=True, verbose_name='Місто')

    # ADDITIONAL INFO
    desc = models.TextField(blank=True, verbose_name='Опис')

    class Meta:
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance).save()