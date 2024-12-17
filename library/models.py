from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    class_name = models.CharField(max_length=50)
    admission_date = models.DateField()

    def __str__(self):
        return self.name
    
class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('borrowed', 'Borrowed'), ('returned', 'Returned')))

    def __str__(self):
        return f"{self.student.name} - {self.book_name}"

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.fee_type}"



