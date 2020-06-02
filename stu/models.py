from django.db import models

# Create your models here.
class teachers(models.Model):
	name = models.CharField(max_length=20,unique=True)

class classes(models.Model):
	name = models.CharField(max_length=20,unique=True)
	m = models.ManyToManyField(teachers,through='teacher_class',through_fields=('classID','teacherID',))

class teacher_class(models.Model):
	classID = models.ForeignKey(classes,on_delete=models.CASCADE)
	teacherID = models.ForeignKey(teachers,on_delete=models.CASCADE)

	class Meta:
		unique_together = ('classID','teacherID',)



class students(models.Model):
	sid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)
	classID = models.ForeignKey(classes,on_delete=models.CASCADE)


class user_info(models.Model):
	alias_name = models.CharField(max_length=20,unique=True)
	real_name = models.CharField(max_length=20)
	pass_word = models.CharField(max_length=32)
	def __str__(self):
		return self.real_name

# class Boy(models.Model):
#     name = models.CharField(max_length=32,unique=True)

# class Girl(models.Model):
#     name = models.CharField(max_length=32,unique=True)
#     m = models.ManyToManyField('Boy',through='Love',through_fields=('g','b'))

# class Love(models.Model):
# 	g = models.ForeignKey('Girl',on_delete=models.CASCADE)
# 	b = models.ForeignKey('Boy',on_delete=models.CASCADE)

# 	class Mate:
# 		unique_together = (('g','b'),)


# class Boy(models.Model):
#     name = models.CharField(max_length=32,unique=True)
#     # m = models.ManyToManyField('Girl')

# class Girl(models.Model):
#     name = models.CharField(max_length=32,unique=True)
#     text = models.CharField(max_length=32)
#     m = models.ManyToManyField('Boy')
