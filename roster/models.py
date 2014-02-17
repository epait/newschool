from django.db import models

# Create your models here.

class Course(models.Model):
	name = models.CharField(unique=True, max_length=50)
	callnumber = models.CharField(unique=False, max_length=4)
	instructor = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	term = models.CharField(max_length=50)
	students = models.ManyToManyField('Student')
	date = models.DateField()

	class Meta(object):
		verbose_name_plural = "Courses"
		ordering = ('-date', 'name')

	def __unicode__(self):
		return U'%s | %s' %(self.callnumber, self.name)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Course, self).save(*args, **kwargs)

class Student(models.Model):
	name = models.CharField(unique=False, max_length=50)
	pid = models.CharField(unique=True, max_length=12)
	grade = models.IntegerField(unique=False, null=True, max_length=3)
	age = models.IntegerField(unique=False, null=True)
	gender = models.CharField(unique=False, null=True, max_length=12)
	email = models.EmailField(unique=False, null=True, max_length=75)
	home_phone = models.CharField(unique=False, null=True, max_length=20)
	cell_phone = models.CharField(unique=False, null=True, max_length=20)
	class_year = models.IntegerField(unique=False, null=True, max_length=4)
	credit_hours_earned = models.IntegerField(unique=False, null=True, max_length=3)
	credit_hours_enrolled = models.IntegerField(unique=False, null=True, max_length=2)
	gpa = models.DecimalField(unique=False, null=True, max_digits=3, decimal_places=2)
	home_address = models.CharField(unique=False, null=True, max_length=300)
	school_address = models.CharField(unique=False, null=True, max_length=300)
	# imageurl = models.ImageField(upload_to='photos/prolfie_pictures/'[, height_field=None, width_field=None, max_length=100])

	class Meta(object):
		ordering = ('pid', 'name')

	def __unicode__(self):
		return U'%s %s' %(self.name, self.pid)