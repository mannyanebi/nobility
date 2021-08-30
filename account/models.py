from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class StudentProfile(models.Model):
    QUALIFICATIONS = [
        ('SECONDARY', 'Secondary'),
        ('BACHELORS', 'Bachelors'),
        ('MASTERS', 'Masters'),
        ('P.HD', 'P.hD'),
    ]

    # create a relationship with User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='student_profile', help_text=_("Your Profile Picture"))
    university = models.CharField(max_length=256, help_text=_("The University You Attended."))
    highest_qualification = models.CharField(max_length=12, choices=QUALIFICATIONS,
                                             help_text= _("Your Highest Qualification Obtained"),
                                             default="Bachelors")

    def __str__(self):
        return self.user.get_full_name()