from django.db import models
from django.utils import timezone 
from extentions.utils import time_Converter

# Create your models here.
# class category(models.Model):
#     title = models.CharField(max_length=100)
#     sluge = models.SlugField(max_length=100,unique=True)
#     status = models.BooleanField()

#my manger
class ArticleManger(models.Manager):
    def Published(self):
        return self.filter(status = 'p')
    
class CategoryManger(models.Manager):
    def Active(self):
        return self.filter(status = True)
        
class Category(models.Model):
    Parent = models.ForeignKey('self' , default= None , null=True , blank= True , on_delete= models.SET_NULL , related_name="childeren" , verbose_name= "زیر دسته ")
    title = models.CharField(max_length=100 , verbose_name="عنوان دسته بندی")
    sluge = models.SlugField(max_length=100,unique=True , verbose_name= "آدرس دسته بندی")
    status = models.BooleanField(max_length=1  , verbose_name= "آيا نمایش داده شود؟")
    position = models.IntegerField(verbose_name= "پوزیشن")
    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['Parent__id','position']
        

    def __str__(self):
        return self.title
    
    objects = CategoryManger()
   



class Article(models.Model):
    STATUS_CHOICES =(
        ('d' , 'پیش نویس'),
        ('p' , 'منتشر شده'),
    )
    
   
    title = models.CharField(max_length=100 , verbose_name="عنوان مقاله")
    sluge = models.SlugField(max_length=100,unique=True , verbose_name= "آدرس")
    description = models.TextField(verbose_name="محتوای مقاله")
    image = models.ImageField(upload_to="images", verbose_name= "تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now , verbose_name= "زمان انتشار")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES , verbose_name= "وضعیت")
    Category = models.ManyToManyField(Category , verbose_name= "دسته بندی", related_name= "Articles")
    class Meta():
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
    
    def jpublish(self):
        return time_Converter(self.publish)
    
    def category_published(self):
        return self.Category.filter (status = True)
    
    objects = ArticleManger()

    


    







