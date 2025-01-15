from django.contrib import admin
from home.models import Article , Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position',"title",'sluge','Parent','status',)
    search_fields = ('sluge', 'title')
    list_filter = (['status'])
    prepopulated_fields= {'sluge' : ('title',)}

admin.site.register(Category , CategoryAdmin)
    

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",'sluge','jpublish','status' , "Category_To_Str")
    search_fields = ('desdescription', 'title')
    list_filter = ("publish","status")
    prepopulated_fields= {'sluge' : ('title',)}
    sortable_by = ['-status','-publish']

    def Category_To_Str(self , obj):
        return ",".join([category.title for category in obj.category_published()])
    
    Category_To_Str.short_description = "دسته بندی"
    Article.jpublish.short_description = "زمان انتشار"
    

    
       
    


admin.site.register(Article , ArticleAdmin)