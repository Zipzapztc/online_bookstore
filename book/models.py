from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BookType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name
    

class Book(models.Model):
    book_number = models.CharField(max_length=30)
    book_name = models.CharField(max_length=50)
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=20)
    publishing_house = models.CharField(max_length=20)
    publishing_time = models.DateField()
    storage_time = models.DateTimeField(auto_now_add=True)
    warehouse_operator = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/books/%Y/%m/%d')
    content = RichTextUploadingField()


    def __str__(self):
        return '<Book:%s>' % self.book_name
    '''
    def get_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})
    '''
    class Meta:
        ordering=['-storage_time']