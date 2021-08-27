from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from account.models import Student


class Achievement(models.Model):
    TYPES = [
        ("High CGPA", "High CGPA"),
        ("Leadership Position", "Leadership Position"),
        ("Academic Scholarship", "Academic Scholarship"),
        ("Extra-curricular Activities", "Extra-curricular Activities"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_achievements',
                                null=True, blank=True,
                                help_text=_("Student(s) Achievements"))
    name = models.CharField(max_length=256, null=True, blank=False, help_text=_("Name of the Achievement"))
    type = models.CharField(max_length=60, choices=TYPES, help_text=_("Type of Achievement"))
    year = models.DateField(null=True, blank=False, help_text=_("Date of Achievement"))

    def __str__(self):
        return self.name
