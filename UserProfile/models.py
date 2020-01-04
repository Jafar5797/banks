from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager



class User(AbstractUser):
	username = None
	name = models.CharField(max_length=50,blank=False,null=False)
	email = models.EmailField(unique=True)
	is_consultant = models.BooleanField(default=False)
	is_spoc = models.BooleanField(default=False)
	is_first_time = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	extra_manager = CustomUserManager()
	#objects = CustomUserManager()

	def __str__(self):
	    return self.name

	class Meta:
	    verbose_name = _('user')
	    verbose_name_plural = _('users')

	def get_full_name(self):
	    full_name = '%s %s' % (self.first_name, self.last_name)
	    return full_name.strip()

	def get_name(self):
	    return self.name

	def get_absolute_url(self):
		return reverse('userdetail',kwargs={"id":self.id})

	def get_user(self, user_id):
	        try:
	            return User.objects.get(pk=user_id)
	        except User.DoesNotExist:
	            return None
