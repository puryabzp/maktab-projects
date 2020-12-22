from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, db_index=True)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    first_name = models.CharField(_('first_name'), max_length=80, blank=True, null=True)
    last_name = models.CharField(_('last_name'), max_length=80, blank=True, null=True)
    melli_code = models.CharField(_('melli_code'), unique=True, db_index=True, max_length=10, blank=True, null=True)
    avatar = models.ImageField(_('avatar'), upload_to='profile/image', blank=True, null=True)
    mobile_number = models.CharField(_('mobile_number'), max_length=13, db_index=True, blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the user full_name.
        """
        return self.first_name + ' ' + self.last_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), related_name='user_addresses',
                             related_query_name='user_addresses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    address = models.CharField(_('address'), max_length=500)
    postal_code = models.IntegerField(_('postal_code'), blank=True, null=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ['-created_at']

    def __str__(self):
        return 'For' + " " + self.user.first_name + ' ' + self.user.last_name


class Email(models.Model):
    to = models.EmailField(_("to"), db_index=True)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    subject = models.CharField(_('subject'), max_length=150)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    body = models.TextField(_('body'))

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        ordering = ['-created_at']

    def __str__(self):
        return 'to' + self.to


class Shop(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), related_name='shops',
                             related_query_name='shops', on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    name = models.CharField(_('name'), max_length=80)
    description = models.TextField(_('body'))
    image = models.ImageField(upload_to='shop/images')

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")
        ordering = ['-created_at']

    def __str__(self):
        return self.name
