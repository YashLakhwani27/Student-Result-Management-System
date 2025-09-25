from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator
# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_numeric = models.IntegerField()
    section = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.class_name} - {self.section}'

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.subject_name} - {self.subject_code}'
    
class Student(models.Model):

    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female')
    )
    name = models.CharField(max_length=50)
    roll_id = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    dob = models.DateField(max_length=50)
    student_class = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    reg_date = models.DateField(auto_now_add=True)
    updation_date = models.DateField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'
    

class SubjectCombination(models.Model):
    student_class = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    status = models.IntegerField(default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.student_class} - {self.subject}'
    
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    marks = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    posting_date = models.DateTimeField(auto_now_add=True)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.student} - {self.subject} - {self.marks}'
    

class Notice(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'


