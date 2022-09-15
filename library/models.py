from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Book_Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self) :
        return  "%s " % (self.category )


class Book(models.Model):
    b_name = models.CharField( max_length=200)
    b_author = models.CharField( max_length=200)
    b_isbn_no  = models.IntegerField()
    b_category = models.ForeignKey(Book_Category,on_delete=models.CASCADE )

    def __str__(self):
        return "%s  %s "%(self.b_name,self.b_isbn_no)
    
